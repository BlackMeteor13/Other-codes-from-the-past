
import csv
from pprint import pprint



file = open("vgsales.csv")
data = csv.DictReader( file )
data = list(data)
for row in data:


 pprint(row)