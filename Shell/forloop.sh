#!/bin/bash

read -p "Enter number : " var

if test $var -eq 0
then
	echo "Entered number is 0"
	echo "Please enter positive integer"
	exit 1
fi
n=$var
for i in 1 2 3 4 5 6 7 8 9 10
do
	echo "$n * $i = ` expr $n \* $i`"
done
