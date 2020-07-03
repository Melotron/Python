import csv
import os
import wget
import requests
import glob

url='https://www.ingo.se/export/price/4'
wget.download(url, 'priser.csv')

fileList = glob.glob('/home/pi/ingo/*.csv')

# https://www.ingo.se/v%C3%A5ra-l%C3%A5ga-priser/aktuella-listpriser
# https://www.ingo.se/export/price/4

with open('priser.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_prices.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

        for row in csv_reader:
            csv_writer.writerow(row)
            pris95 = (row[2].replace(',','.'))
#print('\n')
#print(pris95)


payload1 = {'svalue': (pris95)}

requests.get('http://192.168.1.101:8080/json.htm?type=command&param=udevice&idx=161', params=payload1)

for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)
