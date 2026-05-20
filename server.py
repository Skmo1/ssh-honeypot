import socket
import paramiko
import threading
from fake_shell import executer_commande 
from logger import log_tentative, log_commande
HOST = "0.0.0.0"
PORT = 2222
cle = paramiko.RSAKey(filename="server.key")
class MonServeur(paramiko.ServerInterface) :
    def __init__(self,addr):
        self.addr = addr
    def check_auth_password(self, username, password):
        log_tentative(self.addr,username,password)
        print(f"{username} {password}")
        return paramiko.AUTH_SUCCESSFUL
    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_channel_shell_request(self, channel):
        return True

def gerer_connexion(conn,addr):
    with conn:
        print(f"Connected by {addr}")
        transport = paramiko.Transport(conn)
        transport.add_server_key(cle)
        transport.start_server(server=MonServeur(addr))
        channel = transport.accept()
        while True:
            channel.send(b"root@ubuntu:~# ")
            data = channel.recv(1024)
            if not data:
                break 
            commande = data.decode().strip()
            log_commande(addr,commande)
            resultat_cmd = executer_commande(commande)
            channel.send((resultat_cmd+"\n").encode())
            if commande == "exit":
                break

            print(f"Commande reçue :{commande}")
    
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST,PORT))
    s.listen()
    while True: 
        conn,addr = s.accept()
        t =threading.Thread(target=gerer_connexion,args=(conn,addr))
        t.daemon = True
        t.start()
