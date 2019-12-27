import csv
import WebScraper
import datetime
import threading
import Settings
from time import sleep
    
def run(filepath):
    try:
        print('Loading new price')
        data = WebScraper.loadPrices()
        with open(filepath, 'w') as newFile:
            csvWriter = csv.writer(newFile, delimiter=';', lineterminator='\n')
            for row in data:
                csvWriter.writerow(row)
            print('New price saved to the file')
    except Exception as e:
        print("Exception: " + str(e))

csv.register_dialect('dialect',
delimiter = ';',
lineterminator='\n',
skipinitialspace=True)

while(True):
    dictionary = {}
    interval = 8
    seconds = interval*3600
    filepath = 'prices.csv'
    now = datetime.datetime.now()
    try:
        print('Loading settings')
        dictionary = Settings.loadSettings()
        filepath = dictionary['filepath']
        interval = int(dictionary['interval'])
    except Exception as e:
        print("Exception: " + str(e))
    try:
        nextRun = now + datetime.timedelta(hours=interval)
        nextRun = nextRun.replace(minute=0, second=0)
        seconds = (nextRun-now).total_seconds()
    except Exception as e:
        print("Exception: " + str(e))
    run(filepath)
    print('Going to sleep for ' + str(seconds) + ' seconds')
    sleep(seconds)