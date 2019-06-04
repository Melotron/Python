#!/usr/bin/env python
import paramiko
import os
import zipfile
import tarfile
from datetime import datetime

# Setting Date and time for the upload dating.
now = datetime.now()
date_time = now.strftime("%Y%m%d-%H%M%S")

# EDIT THIS! With your login and password and IP to your server.
username = "LOGIN"
password = "PASSWORD"
host = "IP"

# Its going to start to pack the folder that you secify in the next area.
def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

# What you want to get backedup.
backupdir = ('test/')
if backupdir :
    try:
        zipf = zipfile.ZipFile('/Backup/Backup.zip',mode='w')
        zipdir('test/', zipf)
    except Exception as e:
        print e
    finally:
        zipf.close()

# Now its time to send the file to the server.
# I'm going to date tag the file when I upload it.
# I'am going to add the date string to the zip part later.

port = 22
transport = paramiko.Transport((host, port))

transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Here are the files for uploading and where it will land.
# You can set a specifyed folder for the diferent things you want to backup.
filepath = 'Backup'+date_time+'.zip'
localpath = '/Backup/Backup.zip'
sftp.put(localpath, filepath)
sftp.close()
transport.close()

# Next part are to remove the old file.
# Time to learn how to do that =)
