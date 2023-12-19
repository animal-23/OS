#!/bin/bash
read -p "Enter the number: " n

a=n
b=n
temp1=0
sum=0

while((a>0))
do
a=$((a/10))
temp1=$((temp1+1))
done

while((b>0))
do
temp2=$((b%10))
b=$((b/10))
temp3=$(echo "$temp2^$temp1" | bc)
sum=$((sum+temp3))
done

if(($n== $sum))
then
echo "$n is an armstrong number"
else
echo "$n is not an armstrong number"
fi
