import os
import sys
import requests
import random
import datetime
from bs4 import BeautifulSoup
from rich.console import Console
from rich import print as cetak

# Open-Sourced By Harry Akumaa.

#-----------------[ IMPORT-MODULE ]-------------------#

def modules():
    print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHECKING FOR UPDATES \x1b[37m")

    os.system('pkg update -y && pkg upgrade -y')
    os.system('clear')

    try:
        import requests
    except ModuleNotFoundError:
        print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m INSTALLING REQUESTS \x1b[37m")
        os.system('pip install requests --quiet')

    try:
        import bs4
    except ModuleNotFoundError:
        print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m INSTALLING BS4 \x1b[37m")
        os.system('pip install bs4 --quiet')

    try:
        import rich
    except ModuleNotFoundError:
        print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m INSTALLING RICH \x1b[37m")
        os.system('pip install rich --quiet')

modules()

#------------------[ GLOBAL VARIABLES ]-------------------#

console = Console()
version = 'OPEN SOURCE'
session = requests.Session()

#------------------[ USER-AGENT GENERATION ]-------------------#

user_agents = []
for _ in range(10):
    user_agents.append(
        f"Mozilla/5.0 (Linux; Android {random.randint(6,12)}; en-us; GT-{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
        f"{random.randint(1,999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}) AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.randint(73,100)}.0.{random.randint(4200,4900)}.{random.randint(40,150)} Mobile Safari/537.36"
    )

#------------------[ HELPER FUNCTIONS ]-------------------#

def clear():
    os.system('clear')

def banner():
    print("""  
    ___ ___                     _____.___.
   /   |   \_____ ______________\__  |   |
  /    ~    \__  \\_  __ \_  __ \/    |   |
  \    Y    // __ \|  | \/|  | \/\____   |
   \___|_  /(____  /__|   |__|   / _____|
         \/      \/              \/      
    """)

def info():
    console.print(f"""
    [cyan]----------------------------------------------
    AUTHOR     : Pemba Grgz
    GITHUB     : grgzzv1
    FACEBOOK   : Pemba Grgz
    VERSION    : {version}
    ----------------------------------------------[/cyan]
    """)

#------------------[ LOGIN FUNCTION ]-------------------#

def login():
    clear()
    banner()
    info()

    if os.path.exists("data/.token.txt"):
        with open("data/.token.txt", "r") as file:
            token = file.read().strip()
    else:
        token = None

    if token:
        console.print("[green]✔ Already Logged In[/green]")
    else:
        console.print("[red]✘ No Token Found, Please Login[/red]")
        token = input("[yellow]Enter Token: [/yellow]")
        with open("data/.token.txt", "w") as file:
            file.write(token)
        console.print("[green]✔ Token Saved![/green]")

#------------------[ MAIN MENU ]-------------------#

def menu():
    clear()
    banner()
    info()

    console.print("[cyan]1. Crack Public IDs[/cyan]")
    console.print("[cyan]2. Crack From File[/cyan]")
    console.print("[cyan]3. Check Results[/cyan]")
    console.print("[cyan]0. Logout[/cyan]")

    choice = input("Choose: ")

    if choice == "1":
        console.print("[yellow]Feature Coming Soon![/yellow]")
    elif choice == "2":
        console.print("[yellow]Feature Coming Soon![/yellow]")
    elif choice == "3":
        console.print("[yellow]Feature Coming Soon![/yellow]")
    elif choice == "0":
        os.remove("data/.token.txt")
        console.print("[red]✔ Logged Out Successfully[/red]")
    else:
        console.print("[red]Invalid Option![/red]")
        menu()

#------------------[ SCRIPT EXECUTION ]-------------------#

if __name__ == "__main__":
    login()
    menu()