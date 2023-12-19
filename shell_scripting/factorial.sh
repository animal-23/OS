#!/bin/bash
read -p "Enter the number: " n

fact=1

if((n<=1))
then 
echo 1
else
for((i=2;i<=n;i++))
do
fact=$((fact*i))
done
echo "Factorial of $n is $fact"
fi