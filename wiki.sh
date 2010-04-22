#!/usr/bin/bash

# Set stuff up
WIKI_DIR=/tmp/wiki
mkdir -p $WIKI_DIR

echo "Content-Type: text/html"
echo

get(){
	if [ "x$QUERY_STRING" != "x" -a -r "$WIKI_DIR/$QUERY_STRING" ]
	then
		cat "$WIKI_DIR/$QUERY_STRING"
	else
		echo '<HTML>'
		echo '<BODY>'
		if [ "x$QUERY_STRING" != "x" ]
		then
			echo "<h1>Page Not Found</h1>"
		else
			echo '<h1>Please specify a page</h1>'
		fi
		echo '</BODY>'
		echo '</HTML>'
		echo
	fi
}

post(){
	if [ "x$QUERY_STRING" != "x" ]
	then
		read -n $CONTENT_LENGTH content
		echo -n $content > "$WIKI_DIR/$QUERY_STRING"
	fi
	env |
	while read line
	do
		echo $line "<br/>"
	done
	echo '<hr/>'
	echo $content
}

delete(){
	if [ "x$QUERY_STRING" != "x" -a -r "$WIKI_DIR/$QUERY_STRING" ]
	then
		rm -f "$WIKI_DIR/$QUERY_STRING"
	fi
}

case $REQUEST_METHOD in
	"GET")
		get
		;;
	"PUT")
		post
		;;
	"POST")
		post
		;;
	"DELETE")
		delete
		;;
esac
