#webscraper for cadence apartments to get the pricing of apartments daily
#use with crontab. invoke the crontab editor with; crontab -e
#
# @daily /opt/local/bin/python  /Users/dylanclayton/GitProjects/WebScraper/ApartmentPricing/webscraper.py


import datetime
import json
from lxml import html
import requests


now = datetime.datetime.now()
pricing_folder = "/Users/dylanclayton/GitProjects/WebScraper/ApartmentPricing/pricing/"
filename = "cadence_%d-%d-%d.json" % (now.year, now.month, now.day)

f = open(pricing_folder+filename, "w")


url = "http://www.cadenceapts.com/floor-plans/"
page = requests.get(url+"?bedrooms=1")
tree = html.fromstring(page.content)

rooms = tree.xpath("//figcaption/h2/text()")
floorplans = tree.xpath("//figcaption/h3/text()")
square_feet = tree.xpath("//figcaption/ul/li[2]/text()")
prices = tree.xpath("//figcaption/ul/li[3]/text()")


json_listing = []
for i in xrange(len(rooms)):
    page = requests.get(url+rooms[i])
    tree = html.fromstring(page.content)
    img = tree.xpath("/html/body/div/section[2]/div[2]/figure/img/@src") 

    listing = [ rooms[i], floorplans[i], square_feet[i], prices[i], img[0] ]
    json_listing.append(listing)

json.dump(json_listing, f)

f.close()
