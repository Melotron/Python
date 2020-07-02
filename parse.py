import csv
import os

# https://www.ingo.se/v%C3%A5ra-l%C3%A5ga-priser/aktuella-listpriser
# https://www.ingo.se/export/price/4    Listan som ger priser

with open('historical-prices.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_prices.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

        for row in csv_reader:
            csv_writer.writerow(row)
            priser = (row[2])

print(priser)

os.remove('new_prices.csv')

###
# Time to add payload for domoticz.
#
#requests.get('http://192.168.1.101:8080/json.htm?type=command&param=udevice&idx=22', params=priser)
#
#
