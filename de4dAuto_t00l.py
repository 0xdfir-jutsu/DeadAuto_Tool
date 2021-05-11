# -*- coding: utf-8 -*-
# @Time    : 5/11/2021 8:26 AM
# @Author  : VLBaoNgoc-SE130726
# @Email   : ngocvlbse130726@fpt.edu.vn
# @File    : de4dAuto_t00l.py.py
# @Software: PyCharm
# !/usr/bin/python
# -*- coding: utf-8 -*-
##########################################
#         AUTHOR-GEN-FPTU-2021           #
#                                        #
##########################################
import sys
import os
import time
import signal
from time import sleep
from sys import argv
from platform import system


def sigint_handler(signum, frame):
    os.system("clear")
    print("CTRL+C detected!")
    print(" \033[1;91m@Good bye\033[1;m")
    sys.exit()


signal.signal(signal.SIGINT, sigint_handler)


def logo():
    print("""\033[1;91m

 (                                                                       
 )\ )               (      (               )             )           (   
(()/(     (     )   )\ )   )\       (   ( /(          ( /(           )\  
 /(_))   ))\ ( /(  (()/(((((_)(    ))\  )\()) (  ___  )\()) (    (  ((_) 
(_))_   /((_))(_))  ((_)))\ _ )\  /((_)(_))/  )\|___|(_))/  )\   )\  _   
 |   \ (_)) ((_)_   _| | (_)_\(_)(_))( | |_  ((_)    | |_  ((_) ((_)| |  
 | |) |/ -_)/ _` |/ _` |  / _ \  | || ||  _|/ _ \    |  _|/ _ \/ _ \| |  
 |___/ \___|\__,_|\__,_| /_/ \_\  \_,_| \__|\___/     \__|\___/\___/|_|                                                                         
  Gen - github.com/genethical99/ |_| v1.0
\033[1;m """)

def menu0():
    logo()
    print("""
        1 - Nmap Scan
        2 - DDoS 
        0 - Exit
    """)
def start_Automate():
    menu0()
    print("Enter on of the options.")
    choice = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
    if choice == "1":
        nmap_scan_automate()
    if choice == "2":
        print("")
    if choice == "0":
        print(" \033[1;Gen@Good bye\033[1;m")
        sys.exit()

    else:
        print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(2)
        start_Automate()
def menu1():
    logo()
    print("""
        1-) Default Scan
        2-) Host Discovery
        3-) Port(SYN) Scan
        4-) Port(TCP) Scan
        5-) Port(UDP) Scan
        6-) Port Definition (-sS -F)
        7-) Service and Version Discovery
        8-) OS Analysis and Version Discovery
        9-) Nmap Script Engineering
        \033[1;91m Firewall and IDS bypass \033[1;m
        10-) Spoof Mac (-spoof-mac 'cisco')
        11-) MTU
        \033[1;91m Mixed \033[1;m
        12-) together (-sS -sV -Pn -p-)
        0-) Exit
        """)


def nmap_scan_automate():
    menu1()
    print("   Enter one of the options.")

    secim = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")

    if secim == "1":
        print(" Starting Default Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        birhedef = input("     Enter Your Destination: ")
        os.system("nmap " + birhedef + " -oN " + birhedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimbir = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimbir == "1":
            nmap_scan_automate()
        if secimbir == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "2":
        print(" Starting Host Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        ikihedef = input("     Enter Your Destination: ")
        os.system("nmap -Pn " + ikihedef + " -oN " + ikihedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimiki = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimiki == "1":
            nmap_scan_automate()
        if secimiki == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "3":
        print(" Starting Port(SYN) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        uchedef = input("     Enter Your Destination: ")
        os.system("nmap -sS " + uchedef + " -oN " + uchedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimuc = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimuc == "1":
            nmap_scan_automate()
        if secimuc == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "4":
        print(" Starting Port(TCP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        dorthedef = input("     Enter Your Destination: ")
        os.system("nmap –sT " + dorthedef + " -oN " + dorthedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimdort = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimdort == "1":
            nmap_scan_automate()
        if secimdort == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "5":
        print(" Starting Port(UDP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        beshedef = input("     Enter Your Destination: ")
        os.system("nmap –sU " + beshedef + " -oN " + beshedef + ".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimbes = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimbes == "1":
            nmap_scan_automate()
        if secimbes == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "6":
        print(" Starting Port Definition (-sS -F)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        altihedef = input("     Enter Your Destination: ")
        os.system("nmap -sS -F " + altihedef + " -oN " + altihedef + ".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimalti = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimalti == "1":
            nmap_scan_automate()
        if secimalti == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "7":
        print(" Starting Service and Version Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        yedihedef = input("     Enter Your Destination: ")
        os.system("nmap –sS -F " + yedihedef + " -oN " + yedihedef + ".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimyedi = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimyedi == "1":
            nmap_scan_automate()
        if secimyedi == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "8":
        print(" Starting OS Analysis and Version Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        sekizhedef = input("     Enter Your Destination: ")
        os.system("nmap –sS -O " + sekizhedef + " -oN " + sekizhedef + ".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimsekiz = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimsekiz == "1":
            nmap_scan_automate()
        if secimsekiz == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "9":
        print(" Starting Nmap Script Engineering...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        dokuzhedef = input("     Enter Your Destination: ")
        os.system("nmap –sC " + dokuzhedef + " -oN " + dokuzhedef + ".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimdokuz = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimdokuz == "1":
            nmap_scan_automate()
        if secimdokuz == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "10":
        print("Starting -spoof-mac 'cisco' ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onhedef = input("     Enter Your Destination: ")
        os.system("nmap -spoof-mac 'cisco' " + onhedef + " -oN " + onhedef + ".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimon = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimon == "1":
            nmap_scan_automate()
        if secimon == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "11":
        print("Starting MTU ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onbirhedef = input("     Enter Your Destination: ")
        print("Enter the MTU value. Data payload MTU must be >0 and multiple of 8")
        mtudeger = input("MTU Value:")
        os.system("nmap --mtu " + mtudeger + " " + onbirhedef + " -oN " + onbirhedef + ".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimonbir = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimonbir == "1":
            nmap_scan_automate()
        if secimonbir == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "12":
        print("Starting together (-sS -sV -Pn -p-) ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onikihedef = input("     Enter Your Destination: ")
        os.system("nmap -sS -sV -Pn -p- " + onikihedef + " -oN " + onikihedef + ".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimoniki = input("root""\033[1;Gen@H4ack4Fun:~$\033[1;m ")
        if secimoniki == "1":
            nmap_scan_automate()
        if secimoniki == "2":
            print(" \033[1;Gen@Good bye\033[1;m")
            sys.exit()
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            nmap_scan_automate()

    if secim == "0":
        print(" \033[1;91m@Good bye\033[1;m")
        sys.exit()

    else:
        print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(2)
        nmap_scan_automate()


def rootcontrol():
    start_Automate()
    if os.geteuid() == 0:
        nmap_scan_automate()
    else:
        print("Please run it with root access.")
        sys.exit()

if __name__ == '__main__':
    rootcontrol()
