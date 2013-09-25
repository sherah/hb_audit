from sys import argv

script, filename = argv

f = open(filename)

restaurants = {}
for line in f:
  datalist = line.split(":")
  restaurants[datalist[0]] = int(datalist[1])

sorted_restaurants = sorted(restaurants)

for restaurant in sorted_restaurants:
  print restaurant, restaurants[restaurant]