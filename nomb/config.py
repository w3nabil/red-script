# Lib 
import json

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

# Asking for SMTP 
print("Would you like to \n1) Use a gmail account for attack [Default][Recommended]\n2) or Your own SMTP Server")
choosesmtp = input(" > ") or 1

if int(choosesmtp) == 1:
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
elif int(choosesmtp) == 2:
    print("Please enter SMTP Server Address (Example: smtp.yourserver.com)")
    smtp_server = input(" > ") or print("Can not attack withhblank smtp server address") & exit(1)
    print("Please enter SMTP Server Port Address [Default = 587]")
    smtp_port = int(input(" > ")) or 587

print("Enter SMTP User")
smtp_user = input(" > ")
print("Enter SMTP Password [For Gmail and 2FA Users Please use App Password]")
smtp_password = input(" > ")


data = {}

data['smtp_server'] = smtp_server 
data['smtp_port'] = smtp_port
data['smtp_user'] = smtp_user
data['smtp_password'] = smtp_password

with open('mailconfig.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Updated config.json, Try running 'sudo mailbomb.py'")