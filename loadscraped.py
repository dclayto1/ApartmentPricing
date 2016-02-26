import json

f = open("pricing/cadence_2016-2-26.json", "r")
listings = json.load(f)
f.close()

for each in listings:
    print each
