import socket
import paramiko
HOST = "0.0.0.0"
PORT = 2222
cle = paramiko.RSAKey(filename="server.key")
class MonServeur(paramiko.ServerInterface) :
    def check_auth_password(self, username, password):
        print(f"{username} {password}")
        return paramiko.AUTH_SUCCESSFUL
    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_channel_shell_request(self, channel):
        return True
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        transport = paramiko.Transport(conn)
        transport.add_server_key(cle)
        transport.start_server(server=MonServeur())
        channel = transport.accept()
        while True:
            channel.send(b"root@ubuntu:~# ")
            data = channel.recv(1024)
            if not data:
                break 
            commande = data.decode().strip()
            if commande == "exit":
                break

            print(f"Commande reçue :{commande}")