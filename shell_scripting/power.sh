#!/bin/bash
read -p "Enter base value: " x
read -p "Enter exponent value: " n

temp=1
for((i=0;i<n;i++))
do 
temp=$((temp*x))
done 
echo "$x to the power of $n is $temp"

temp2=$(echo "$x^$n" | bc)
echo $temp2