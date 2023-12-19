#!/bin/bash
echo "enter the directory name"
read dir
if [ -d $dir ]
then
cd $dir
fi
echo "Files in the current directory with read, write, and execute permissions:"
find . -maxdepth 1 -type f -perm -u=rwx
