import json
import csv

with open('data.json') as f:
    data = json.load(f)

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data[0].keys())

    for row in data:
        writer.writerow(row.values())
