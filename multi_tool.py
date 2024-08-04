#!usr/bin/python3
#pip3 install python-nmap

import sqlite3
import os 
from colorama import Fore
import colorama
import nmap
import time

# Création ou connexion à la base de données SQLite
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Création de la table des utilisateurs si elle n'existe pas
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
)
''')

# Fonction pour ajouter un nouvel utilisateur
def create_user():
    username = input("Veuillez entrer un nom d'utilisateur: ")
    try:
        c.execute('INSERT INTO users (username) VALUES (?)', (username,))
        conn.commit()
        print("Utilisateur ajouté avec succès.")
    except sqlite3.IntegrityError:
        print("Ce nom d'utilisateur existe déjà.")

# Fonction pour vérifier l'utilisateur et se connecter
def login():
    username = input("Veuillez entrer votre nom d'utilisateur pour vous connecter: ")
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    if user:
        print(f"Bienvenue, {username}!")
        tool_menu()
        time.sleep(2)
    if os.name == 'nt':  # Pour Windows
        os.system('cls || clear')
    else:
        print("Nom d'utilisateur non trouvé. Accès refusé.")
        
# Menu principal des outils
def tool_menu():
    print("Vous êtes maintenant connecté à l'outil.")
    print(Fore.BLUE + '''
 ▄▄▄      ▒███████▒ ▒█████  ▄▄▄█████▓ ██░ ██ 
▒████▄    ▒ ▒ ▒ ▄▀░▒██▒  ██▒▓  ██▒ ▓▒▓██░ ██▒  [!] Info tool
▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██░  ██▒▒ ▓██░ ▒░▒██▀▀██░
░██▄▄▄▄██   ▄▀▒   ░▒██   ██░░ ▓██▓ ░ ░▓█ ░██ 
 ▓█   ▓██▒▒███████▒░ ████▓▒░  ▒██▒ ░ ░▓█▒░██▓
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒░ ▒░▒░▒░   ▒ ░░    ▒ ░░▒░▒
  ▒   ▒▒ ░░░▒ ▒ ░ ▒  ░ ▒ ▒░     ░     ▒ ░▒░ ░
  ░   ▒   ░ ░ ░ ░ ░░ ░ ░ ▒    ░       ░  ░░ ░
      ░  ░  ░ ░        ░ ░            ░  ░  ░
          ░                                   ''')
    print("Choissisez une option ci-dessous")
    n = input("1-Scanner Résaux\n2-Detection Vulnerabilité\n3- Exploit")
    if n == "1":
        nmap()
    if n == "2":
        vuln()
    if n == "3":
        os.system("msfconsole")
    if n == "!":
        info()
    else :
        print("\nChoisissez un nombre entre 1 et 4 (4 = 0)")

# Menu principal
def menu_principale():
    print(Fore.RED + '''
 ▄▄▄      ▒███████▒ ▒█████  ▄▄▄█████▓ ██░ ██ 
▒████▄    ▒ ▒ ▒ ▄▀░▒██▒  ██▒▓  ██▒ ▓▒▓██░ ██▒
▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██░  ██▒▒ ▓██░ ▒░▒██▀▀██░
░██▄▄▄▄██   ▄▀▒   ░▒██   ██░░ ▓██▓ ░ ░▓█ ░██ 
 ▓█   ▓██▒▒███████▒░ ████▓▒░  ▒██▒ ░ ░▓█▒░██▓
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒░ ▒░▒░▒░   ▒ ░░    ▒ ░░▒░▒
  ▒   ▒▒ ░░░▒ ▒ ░ ▒  ░ ▒ ▒░     ░     ▒ ░▒░ ░
  ░   ▒   ░ ░ ░ ░ ░░ ░ ░ ▒    ░       ░  ░░ ░
      ░  ░  ░ ░        ░ ░            ░  ░  ░
          ░                                   ''')
    b = input("Choisissez une option:\n1. Créer un utilisateur\n2. Se connecter\n0. Quitter")
    if b == '1':
        create_user()
    elif b == '2':
        login()
    elif b == '0':
        print("Au revoir!")
        exit()
    else:
            print("Option invalide, veuillez réessayer.")

def nmap():
    print(Fore.GREEN + """
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝     ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                        Bienvenue dans le Scanner résaux
          """)
    # TypeError: 'str' object is not callable
    ip = input('PLease enter the Ip address')
    sc.scan(ip , '1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

def vuln():
    print(Fore.CYAN + """
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗██████╗  █████╗ ██████╗ ██╗██╗     ██╗████████╗██╗███████╗███████╗\n
██║   ██║██║   ██║██║     ████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║██║     ██║╚══██╔══╝██║██╔════╝██╔════╝\n
██║   ██║██║   ██║██║     ██╔██╗ ██║█████╗  ██████╔╝███████║██████╔╝██║██║     ██║   ██║   ██║█████╗  ███████╗\n
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║██╔══██╗██║██║     ██║   ██║   ██║██╔══╝  ╚════██║\n
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║██████╔╝██║███████╗██║   ██║   ██║███████╗███████║\n
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝\n
                                                                                                              
        ██████╗ ███████╗████████╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗\n
        ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║\n
        ██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║\n
        ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║\n
        ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║\n
        ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n
""")
    # TypeError: 'str' object is not callable
    ip = input("\nVeuiller entré l'addresse Ip")
    print(os.system('nmap -sV --script=vulcan.nse' +ip ))

def info():
    print('''
name_tool = "Azoth"
version_tool = "1.1"
coding_tool = "Python 3"
language_tool = "EN"
creator = "000-Darkstar"
platform = "Windows 10/11 & Linux"
website = "soon.."
github_tool = "soon.."
license = "https://github.com/000-DarkStar/Azoth-Tool/LICENSE"
copyright = "Copyright (c) Azxth 'LICENSE'"
          ''')
    timeout=5
    print(tool_menu)


    # Création ou connexion à la base de données SQLite
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Création de la table des utilisateurs si elle n'existe pas
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
)
''')

def main():
        print("\n--- Menu Principal ---")
        print("1. Créer un utilisateur")
        print("2. Se connecter")
        print("0. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            login()
        elif choice == '0':
            print("Au revoir!")
            exit()
        else:
            print("Option invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()

# Fermeture de la connexion à la base de données
conn.close()
