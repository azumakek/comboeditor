import string
import hashlib
import requests
import random
import os
import time

def userpass():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        fullstring = line.split(":")
        email = fullstring[0]
        password = fullstring[1]
        emailstring = email.split("@")
        emailfinal = emailstring[0]
        print(emailfinal + ":" + password)
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()
    
def ex2pw():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        print(line + "!")
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()
    
def one2pw():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        print(line + "1")
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()
    
def onetwothree2pw():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        print(line + "123")
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()
    
def dollar2pw():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        print(line + "$")
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()
    
def addall():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        print(line + "!")
        print(line + "1")
        print(line + "123")
        print(line + "$")
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()

    
def domainchanger():
    os.system('clear')
    filename = input("Filename > ")
    domain = input("Domain to change to (Without @) > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line2 = line.split(":")
        password = line2[1]
        emailstring = line2[0]
        emailstring2 = emailstring.split("@")
        emailusername = emailstring2[0]
        print(emailusername + "@" + domain + ":" + password)
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()

def passfirstcapital():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line2 = line.split(":")
        password = line2[1]
        email = line2[0]
        print(email + ":" + password.title())
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()
    
def userpassreverse():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line2 = line.split(":")
        user = line2[0]
        password = line2[1]
        print(password + ":" + user)
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()
        
def emailpassreverse():
    os.system('clear')
    filename = input("Filename > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line2 = line.split(":")
        email = line2[0]
        password = line2[1]
        print(password + ":" + email)
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()

def rmpwlessthan():
    os.system('clear')
    filename = input("Filename > ")
    rmlength = input("Remove passwords less than > ")
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line2 = line.split(":")
        email = line2[0]
        password = line2[1]
        if len(password) >= int(rmlength):
            print(line)
    print("\n\n10 seconds until returning to menu...")
    time.sleep(10)
    option()
        
def option():
    os.system('clear')
    option = input("Coded by Azuma with <3 -- https://azuma.dev\n\nA certain someone will try crack this tool - his dox can be found @ https://ghostbin.co/paste/j9ytv\n\nThis tool can be found OPEN SOURCE at https://github.com/azumakek/comboeditor\n\n-------------------------------------------------------------\n\nChoose your module :)\n\n[1] Email:Pass to User:Pass\n[2] Add ! to Password\n[3] Add 1 to Password\n[4] Add 123 to Password\n[5] Add $ to Password\n[6] Add !, 1, 123 and $ to password, one by one\n[7] Domain Changer\n[8] Change the first letter of the password to capital\n[9] Reverse User:Pass to Pass:User\n[10] Reverses Email:Pass to Pass:Email\n[11] Remove lines that contain passwords less than a certain length [Good for sites with password requirements]\n\n")
    if option == "1":
        userpass()
    if option == "2":
        ex2pw()
    if option == "3":
        one2pw()
    if option == "4":
        onetwothree2pw()
    if option == "5":
        dollar2pw()
    if option == "6":
        addall()
    if option == "7":
        passfirstcapital()
    if option == "8":
        passfirstcapital()
    if option == "9":
        userpassreverse()
    if option == "10":
        emailpassreverse()
    if option == "11":
        rmpwlessthan()


os.system('clear')  
auth = input("Auth key > ")

hash1 = hashlib.md5(auth.encode()) 
hash2 = hash1.hexdigest() 

r = requests.get("https://www.nulled.to/misc.php?action=validateKey&authKey=" + str(hash2))
if "success" in r.text:
    print("Success! Redirecting to tool now...")
    os.system('clear')
    option()
else:
    print("Wrong auth key")
    quit()