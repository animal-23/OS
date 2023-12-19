#!/bin/bash
string1="Hello"
string2="hello"
if (( "$string1" = "$string2" ))
then
echo "The strings are equal."
else
echo "The strings are not equal."
fi
