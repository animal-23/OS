#!/bin/bash
for arg in "$@"; do
if [ -f "$arg" ];
then
echo "$arg is a file." num_lines=$(wc -l < "$arg")
echo "Number of lines in $arg: $num_lines" elif [ -d "$arg" ];
echo "$arg is a directory."
else
echo "$arg is neither a file nor a directory."
fi
done
