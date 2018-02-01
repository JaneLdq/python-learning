import csv

csvFile = open("test.csv", 'w+')

try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number+2', 'number*2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()
