import json
import sys


if len(sys.argv) != 2:
    print "Incorrect usage. Please specify json file in pricing/ as an argument..."
    sys.exit(0)

f = open(sys.argv[1], "r")
listings = json.load(f)
f.close()

for each in listings:
    print each
