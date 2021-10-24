#!/usr/bin/python
import os
import yagmail

#path to log
path='/var/log/auth.log'

#adjust error for find
error = "xxx" 

#adjust email sender
notify = 'xxx@xxx

#adjust email reciver
glogin = 'xxx'
gpass = 'xxx'

def mail(error,notify,glogin,gpass):
    yag = yagmail.SMTP(glogin, gpass)
    contents = [
        "ERROR in /var/log/auth.log: ", error #adjust message
    ]
    yag.send(notify, 'ERROR in auth.log', contents) #add topic



with open(path, 'r') as f:
    for line in f:
        if "error" in line:
            x += line + "\n"

mail(error,notify,glogin,gpass)


