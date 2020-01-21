from random import choice, randrange
import smtplib

print("Loading...")
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', 
'2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '#', '$', 
'%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', 
'\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?']
secret_key = ''

print("Generating SECRET_KEY...")
for x in range(0, randrange(32, 64)):
    secret_key += choice(char)

print("Writing SECRET_KEY to learning_log/secret_key.txt...")
with open('learning_log/secret_key.txt', 'wt') as f:
    f.write(secret_key)
    
print("Change SECRET_KEY is OK.Restart the server to update the SECRET_KEY.")

while True:
    mail_password = input("\nPlease input your mail password:")
    print("Checking your mail password...")
    server = smtplib.SMTP_SSL('smtp.sina.com')
    server.set_debuglevel(1)
    server.starttls()
    try:
        server.login('26922dd@sina.com', mail_password)
    except Exception as e:
        server.quit()
        print("Error:", e, "\nPlease try agian.")
    else:
        server.quit()
        break

print("Writing MAIL_PASSWORD to learning_log/mail_password.txt...")
with open('learning_log/mail_password.txt', 'wt') as f:
    f.write(mail_password)

print("Change MAIL_PASSWORD is OK.Restart the server to update the MAIL_PASSWORD.")

print("\nExit.")
exit()