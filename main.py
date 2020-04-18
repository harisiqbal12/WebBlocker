import time
from datetime import datetime as dt
import shutil
import os 
    
src = "C:/Users/haris/Documents/PYTHON PROJECTS/Webblocker/hosts"
dest = "C:/Windows/System32/drivers/etc/hosts"

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list = ["\nwww.facebook.com","facebook.com","www.facebook.com","www.youtube.com","youtube.com","www.facebook.com","facebook.com","www.udemy.com"]

running = True
while running:
    if dt(dt.now().year, dt.now().month, dt.now().day, 18) <= dt.now() <= dt(dt.now().year, dt.now().month, dt.now().day, 24):
        print("Working Hours")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect}  {website}\n")
        shutil.copy(src, dest)
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Time! ")
        shutil.copy(src, dest)
    

    time.sleep(5)