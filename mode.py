import csv
from collections import Counter
with open('SOCR-HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)

