#!/bin/bash
read -p "Enter no of elements required: " n

arr=(0 1)

for((i=2;i<n;i++))
do
arr[$i]=$((arr[$i-1]+arr[$i-2]))
done 

echo "Fibonacci series: "
for i in ${arr[*]}
do
echo $i
done
