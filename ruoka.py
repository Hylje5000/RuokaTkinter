## Imports
import feedparser
import datetime
import sys


## Setting RSS feed for feedparser and parse it
try:
    url = 'https://ruokalistatkoulutjapaivakodit.arkea.fi/rss/2/1/79be4e48-b6ad-e711-a207-005056820ad4'
    feed = feedparser.parse(url)
except:
    print("Parsing RSS feed resulted in error! Are you connected to the internet?")
    sys.exit()

## Get date and weekday
try:
    day = datetime.datetime.today().weekday()
except:
    print("Getting day resulted in error!")
    sys.exit()

if day == 0:
    daystring = "Maanantai"
elif day == 1:
    daystring = "Tiistai"
elif day == 2:
    daystring = "Keskiviikko"
elif day == 3:
    daystring = "Torstai"
elif day == 4:
    daystring = "Perjantai"
elif day == 5:
    daystring = "Lauantai"    
elif day == 6:
    daystring = "Sunnuntai"

##Printing title for app
print(feed.feed.title)
print('*' * 15)
print('Arkea Ruokalista')
print('*' * 15)
print("Tänään on: " + daystring)
print('*' * 15)

if day < 5:
    viikonloppu = False
    ruoka = feed.entries[day].summary_detail.value
    stringed = str(ruoka)
    splitted = stringed.split('. ')
    print(splitted[0])
    print(splitted[1])
else:
    viikonloppu = True
    splitted = "Viikonloppu POJAT!"
    stringed = ""
    print(splitted)
    print('*' * 15)
