#!usr/bin/python3
#pip3 install python-nmap

import sqlite3
import os 
from colorama import Fore
import colorama
import nmap
import time
import requests
from bs4 import BeautifulSoup

# Création ou connexion à la base de données SQLite
conn = sqlite3.connect('users.db')
c = conn.cursor()

sc = nmap.PortScanner()

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
        os.system('cls')
    else:
        print("Nom d'utilisateur non trouvé. Accès refusé.")
        time.sleep(3)
        
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
    
    ul = input("\n [1] Scan WebSite\n[2] Scan Ip")
    if ul == '1':
        url()
    if ul == '2':
        ip = input("\nVeuiller entré l'addresse Ip")
        print(os.system('nmap -sV --script=vulscan.nse' +ip ))

def info():
    print('''
name_tool = "Azoth"
version_tool = "1.5"
coding_tool = "Python 3"
language_tool = "EN/FR"
creator = "000-DarkStar"
platform = "Windows 10/11 & Linux"
website = "soon.."
github_tool = "soon.."
license = "https://github.com/loxyteck/RedTiger-Tools/blob/main/LICENSE"
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

def check_xss(url):
    test_script = "<script>alert('XSS')</script>"
    response = requests.get(url + test_script)
    if test_script in response.text:
        print(f"[VULNERABLE] XSS vulnerability detected at {url}")
    else:
        print(f"[SAFE] No XSS vulnerability at {url}")

def check_sql_injection(url):
    test_payload = "' OR '1'='1"
    response = requests.get(url + test_payload)
    if "syntax" in response.text or "SQL" in response.text:
        print(f"[VULNERABLE] SQL Injection vulnerability detected at {url}")
    else:
        print(f"[SAFE] No SQL Injection vulnerability at {url}")

def check_file_inclusion(url):
    test_payload = "../../../../etc/passwd"
    response = requests.get(url + test_payload)
    if "root:x" in response.text:
        print(f"[VULNERABLE] File Inclusion vulnerability detected at {url}")
    else:
        print(f"[SAFE] No File Inclusion vulnerability at {url}")

def scan_site(url):
    print(f"Scanning {url} for vulnerabilities...")
    check_xss(url)
    check_sql_injection(url)
    check_file_inclusion(url)

def url():
    target_url = input("Enter the URL of the site to scan: ")
    scan_site(target_url)

if __name__ == "__main__":
    main()

# Fermeture de la connexion à la base de données
conn.close()
