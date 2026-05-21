# SSH Honeypot

Simulation d'un serveur SSH factice en Python permettant de capturer 
les tentatives de connexion et les commandes des attaquants.
## Ce que j'ai appris

- Le fonctionnement du protocole SSH
- L'utilisation de la bibliothèque Paramiko
- Le multithreading en Python
- La programmation orientée objet (classes, héritage)
- La gestion des sockets réseau
- Le logging en Python

## Installation

1. Cloner le repo
git clone https://github.com/Skmo1/ssh-honeypot.git

2. Installer les dépendances
pip3 install paramiko

3. Générer la clé SSH
ssh-keygen -t rsa -b 2048 -f server.key -N ""

4. Lancer le serveur
python3 server.py
## Structure

- `server.py` — gère les connexions SSH entrantes et le threading
- `fake_shell.py` — simule les réponses aux commandes Linux
- `logger.py` — enregistre les tentatives de connexion et les commandes
- `logs/` — contient les fichiers de logs générés
## ⚠️ Avertissement

Ce projet est à but éducatif uniquement. Toute utilisation sur un réseau 
sans autorisation explicite de l'administrateur est illégale et déclinée.
