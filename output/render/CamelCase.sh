#!/usr/bin/bash

while read line
do
	echo $line|
	sed 's/\<[A-Z][a-z]\+[A-Z][a-z][A-Za-z]*\>/<a href="occam.py?\0">\0<\/a>/g'
done

