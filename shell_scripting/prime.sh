#!/bin/bash
read -p "Enter the number: " n

flag=1

if((n<=1))
then
flag=0
elif((n<=3))
then
flag=1
fi 

for((i=2;i<n;i++))
do
if(($n%i==0))
then
flag=0
fi
done

if(($flag==0))
then
echo "$n is not a prime"
else
echo "$n is a prime number"
fi
