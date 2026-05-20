from datetime import datetime
def log_tentative(addr,username,password):
    with open("logs/session.log","a") as file:
        file.write(f"{addr} |{username} |{password} |{datetime.now()} \n")
def log_commande(addr,commande):
    with open("logs/commands.log","a") as file:
        file.write(f"{addr} | {commande} | {datetime.now()} \n")


        
