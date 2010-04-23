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

def do_pull():
	if os.path.isfile(filepath):
		contentFile = open(filepath)
		content = contentFile.read()
	else:
		content = ''
	sys.stdout.write(content)

def do_push():
	content = sys.stdin.read()
	if (content != None) and (content != ''):
		contentFile = open(filepath, 'w')
		contentFile.write(content)
		contentFile.close()
	else:
		do_remove()

def do_remove():
	if os.path.isfile(filepath):
		os.remove(filepath)

def fail():
	sys.exit(1)

if (len(sys.argv) < 2):
	fail()

actions = {
		'-pull': do_pull,
		'-push': do_push,
		'-remove': do_remove,
		}

actions.get(sys.argv[1].lower(), fail)()

