#!/bin/bash
echo "Calculator Menu:"
echo "1.Addition"
echo "2.Substration"
echo "3.Multiplication"
echo "4.Normal division"
echo "5.Integer division"
echo "6.Modular division (Remainder)"
echo "7.Power (Exponent)"

read -p "Enter the index of operator: " op
read -p "Enter first operand: " a
read -p "Enter second operand: " b

case $op in
1) result=$((a+b))
echo "$a + $b = $result";;
2) result=$((a-b))
echo "$a - $b = $result";;
3) result=$((a*b))
echo "$a * $b = $result";;
4) result=$(echo "scale=2; $a / $b" | bc)
echo "$a / $b = $result";;
5) result=$((a/b))
echo "$a // $b = $result";;
6) result=$((a%b))
echo "$a % $b = $result";;
7) result=$(echo "$a ^ $b" | bc)
echo "$a ^ $b = $result";;
esac