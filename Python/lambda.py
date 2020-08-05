#!/usr/bin/python

li = [12, 65, 54, 39, 102, 339, 221, 50, 70, 26]

output = list(filter(lambda x: (x % 13 == 0),li))
print(output)
