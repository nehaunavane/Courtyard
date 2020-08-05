#!/usr/bin/python

b = [5, 4, 4, 3, 1, -1, -3 -5]
sum = 0

i = 0
while True:
    sum += b[i]
    i += 1
    if b[i] <= 0:
        break
print(sum)
