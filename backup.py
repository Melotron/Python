#!/usr/bin/env python
import os
import zipfile
from datetime import datetime
import tarfile
now = datetime.now()
date_time = now.strftime("%Y%m%d-%H%M%S")

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

backupdir = ('test/')
if backupdir :
    try:
        zipf = zipfile.ZipFile('/Backup/''Backup'+date_time+'.zip',mode='w')
        zipdir('test/', zipf)
    except Exception as e:
        print e
    finally:
        zipf.close()
