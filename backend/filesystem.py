#!/usr/bin/env python

import os
import sys

WIKI_DIR='/tmp/wiki'
query_string = os.getenv('QUERY_STRING')
if query_string == '':
	path = 'Home'
else:
	path = query_string.split('&', 1)[0]
filepath = os.path.join(WIKI_DIR, path)
if os.path.isfile(filepath):
	contentFile = open(filepath)
	content = contentFile.read()
else:
	content = ''
sys.stdout.write(content)

