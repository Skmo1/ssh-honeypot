def executer_commande(commande) :
    if commande == "whoami":
        return "root"
    elif commande == "ls":
        return "Documents  Downloads  Music  Pictures  Videos  notes.txt  todo.md" 
    elif commande == "pwd":
        return "/root"
    else:
        return f"bash: {commande} : commande introuvable"

