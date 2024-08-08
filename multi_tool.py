#!usr/bin/python3
#pip3 install python-nmap

import sqlite3
import os 
from colorama import Fore
import colorama
import time
import requests
from bs4 import BeautifulSoup
import nmap

# Création ou connexion à la base de données SQLite
conn = sqlite3.connect('users.db')
c = conn.cursor()


sc = nmap.PortScanner

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
        menu_principale()
    except sqlite3.IntegrityError:
        print("Ce nom d'utilisateur existe déjà.")
        menu_principale()

# Fonction pour vérifier l'utilisateur et se connecter
def login():
    username = input("Veuillez entrer votre nom d'utilisateur pour vous connecter: ")
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    if user:
        print(f"Bienvenue, {username}!")
        tool_menu()
        time.sleep(2)

    else:
        print("Nom d'utilisateur non trouvé. Accès refusé.")
        time.sleep(3)
        exit()
        
# Menu principal des outils
def tool_menu():
    print("Vous êtes maintenant connecté à azoth.")
    print(Fore.BLUE + '''
           _____                        __    .__            [!] INFO TOOLS 
          /  _  \   ________   ____   _/  |_  |  |__          
         /  /_\  \  \___   /  /  _ \  \   __\ |  |  \         
        /    |    \  /    /  (  <_> )  |  |   |   Y  \        
        \____|__  / /_____ \  \____/   |__|   |___|  /        
                \/        \/                       \/         
        ''')
    n = input("1-Scanner Résaux\n2-Detection Vulnerabilité\n3- Exploit\nChoissisez une option: ")
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
        time.sleep(1.5)
    if os.name == 'nt':  # Pour Windows
        os.system('cls')

    else :  # Pour Linux/Mac
        os.system('clear')

# Menu principal
def menu_principale():
    print(Fore.RED + '''
                                  )      )                )     
                       (       ( /(   ( /(     *   )   ( /(     V1.1
                       )\      )\())  )\())  ` )  /(   )\())    
                    ((((_)(   ((_)\  ((_)\    ( )(_)) ((_)\     
                     )\ _ )\   _((_)   ((_)  (_(_())   _((_)    
                     (_)_\(_) |_  /   / _ \  |_   _|  | || |    
                      / _ \    / /   | (_) |   | |    | __ |    
                     /_/ \_\  /___|   \___/    |_|    |_||_|    
                                             ''')
    b = input("\n1. Créer un utilisateur\n2. Se connecter\n0. Quitter\nChoose un number:")
    if b == '1':
        create_user()
    elif b == '2':
        login()
    elif b == '0':
        print("Au revoir!")
        time.sleep(1.3)
        exit()
    else:
        print("Option invalide, veuillez réessayer.")

def nmap():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')

    else :  # Pour Linux/Mac
        os.system('clear')
    print(Fore.GREEN + """
            ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
            ▐                  __                             __     ▌
            ▐  ____    ____  _/  |_ __  _  __  ____  _______ |  | __ ▌
            ▐ /    \ _/ __ \ \   __\\ \/ \/ / /  _ \ \_  __ \|  |/ / ▌
            ▐|   |  \\  ___/  |  |   \     / (  <_> ) |  | \/|    <  ▌
            ▐|___|  / \___  > |__|    \/\_/   \____/  |__|   |__|_ \ ▌
            ▐     \/      \/                                      \/ ▌
            ▐                                                        ▌
            ▐    _____   _____ _____     ____                        ▌
            ▐   /  ___/_/ ___\ \__  \   /    \                       ▌
            ▐   \___ \ \  \___  / __ \_|   |  \                      ▌
            ▐  /____  > \___  >(____  /|___|  /                      ▌
            ▐       \/      \/      \/      \/                       ▌
            ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
                       ╔═════════════════╗
                       ║  Network Scan   ║ V1.1
                       ╚═════════════════╝                 
          """)
    # TypeError: 'str' object is not callable
    ip = input('Please enter the Ip address')
    sc.scan(ip , '1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

def vuln():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')

    else :  # Pour Linux/Mac
        os.system('clear')
    print(Fore.LIGHTMAGENTA_EX + """
        ╔════════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║              .__                                   ___.    .__ .__   .__     __   .__                  ║
        ║___  __ __ __ |  |    ____    ____  _______ _____   \_ |__  |__||  |  |__|  _/  |_ |__|  ____    ______  ║
        ║\  \/ /|  |  \|  |   /    \ _/ __ \ \_  __ \\__  \   | __ \ |  ||  |  |  |  \   __\|  |_/ __ \  /  ___/  ║
        ║ \   / |  |  /|  |__|   |  \\  ___/  |  | \/ / __ \_ | \_\ \|  ||  |__|  |   |  |  |  |\  ___/  \___ \  ║
        ║  \_/  |____/ |____/|___|  / \___  > |__|   (____  / |___  /|__||____/|__|   |__|  |__| \___  >/____  > ║
        ║                         \/      \/              \/      \/                                 \/      \/  ║
        ║                                                                                                        ║                                                                                                        ║
        ║     __           __                     __   .__                                                       ║
        ║  __| _/  ____  _/  |_   ____    ____  _/  |_ |__|  ____    ____                                        ║
        ║ / __ | _/ __ \ \   __\_/ __ \ _/ ___\ \   __\|  | /  _ \  /    \                                       ║
        ║/ /_/ | \  ___/  |  |  \  ___/ \  \___  |  |  |  |(  <_> )|   |  \                                      ║
        ║\____ |  \___  > |__|   \___  > \___  > |__|  |__| \____/ |___|  /                                      ║
        ║     \/      \/             \/      \/                         \/                                       ║
        ╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                                            ╔════════════════════╗
                                            ║    VULN DETECT     ║ V1.1
                                            ╚════════════════════╝
          """)
    # TypeError: 'str' object is not callable
    
    ul = input("\n [1] Scan WebSite\n[2] Scan Ip\n\nEntrer une option: ")
    if ul == '1':
        os.system("sqlmap")
    if ul == '2':
        ip = input("\nVeuiller entré l'addresse Ip: ")
        print(os.system('nmap -sV --script=vulscan.nse' + ip ))

def info():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')

    else :  # Pour Linux/Mac
        os.system('clear')
    print('''
name_tool = "Azoth"
version_tool = "1.5"
coding_tool = "Python 3"
language_tool = "EN/FR"
creator = "000-DarkStar"
platform = "Windows 10/11 & Linux"
website = "soon.."
github_tool = "https://github.com/000-DarkStar/Azoth-Tool/edit/main/multi_tool.py"
license = "https://github.com/000-DarkStar/Azoth-Tool/blob/main/LICENSE"
copyright = "Copyright (c) Azxth 'LICENSE'"
          ''')
    time.sleep(13)
    tool_menu()


    # Création ou connexion à la base de données SQLite
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Création de la table des utilisateurs si elle n'existe pas
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
)
''')

if __name__ == "__main__":
    menu_principale()


# Fermeture de la connexion à la base de données
conn.close()

