import csv
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
for x in cars:
    print(x)
print("  ")
print(cars[1])

with open("MLDATA.csv", 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)

