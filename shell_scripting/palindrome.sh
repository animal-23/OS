#!/bin/bash
read -p "Enter the number: " n

a=n
temp1=0

while((a))
do
temp2=$((a%10))
a=$((a/10))
temp1=$((temp1*10+temp2))
done

if((temp1==n))
then
echo "$n is a palindrome number"
else 
echo "$n is not a palindrom number"
fi