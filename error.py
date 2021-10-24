#!/usr/bin/python
import os
import yagmail

#path to log
path='/var/log/auth.log'

x = "" 

#adjust email reciver
notify = 'xxx@xxx

#adjust email sender
glogin = 'xxx'
gpass = 'xxx'

def mail(error,notify,glogin,gpass):
    yag = yagmail.SMTP(glogin, gpass)
    contents = [
        "ERROR in /var/log/auth.log: ", error #adjust message body
    ]
    yag.send(notify, 'ERROR in auth.log', contents) #add topic



with open(path, 'r') as f:
    for line in f:
        if "error" in line:
            x += line + "\n"

mail(x,notify,glogin,gpass)


