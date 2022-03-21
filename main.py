
import csv
with open('data.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    for i in row:
      print(chr(int(i)+1), end="")
    print()
