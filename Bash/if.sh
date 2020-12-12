#!/bin/bash

echo -n "Enter a number: "
read VAR

if [[ $VAR -lt 0 ]]
then
    echo "Veuillez mettre un nombre positif"
elif [[ $VAR -ge 0 && $VAR -le 9 ]]
then
    echo "1 seul digit !"
elif [[ $VAR -ge 10 && $VAR -le 99 ]]
then
    echo "2 digit !"
elif
    [[ $VAR -ge 100 && $VAR -le 999 ]]
then
    echo "3 digit !"
else
    echo "Au dela de 3 digit !"
fi