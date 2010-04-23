#!/bin/bash

while read line
do
	echo $line|
	sed "s/\<[A-Z][a-z]\+[A-Z][a-z][A-Za-z]*\>/<a href=\"$(echo ${SCRIPT_NAME} | sed 's/\//\\\//g')?\0\">\0<\\/a>/g"
done

