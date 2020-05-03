#!/bin/bash

echo -n "Enter numnber : "
read n

if [[ -n ${n//[0-9]/} ]]; then
    echo "Input Contains letters!  Please enter number : "

exit
fi

rem=$(( $n % 2 ))


if [ $rem -eq 0 ]
then
  echo "$n is even number"
else
  echo "$n is odd number"
fi
