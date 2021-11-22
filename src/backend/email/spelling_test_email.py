"""
Edited by: Joe
Date edited: 22/11/21
function for creating,sending and returning a randomly generated 2 factor authenication code
"""
import smtplib, ssl,random,string
#imports necessary libraries

def send_email(user_email):
    port = 465
    password = "ietyxvyiedswudze"
    sender_email="userverifaction@gmail.com"
    receiver_email=user_email
    code=""
    message = """\
Subject: Spelling Test User Verification

Your two step verification code is """""
    
    for i in range(6):
        operation = random.randint(0,1)
        if operation == 0:
            code = code+str(random.randint(0,9))
        else:
            code = code+random.choice(string.ascii_letters)
    message = message+code
    context = ssl.create_default_context()
    # Create a secure SSL context

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("userverifaction@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
        return(code)

