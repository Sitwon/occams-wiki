#!/usr/bin/env python

import os
import sys
import cgi
import cgitb
cgitb.enable()

WIKI_DIR='/tmp/wiki'
if not os.path.isdir(WIKI_DIR):
	os.makedirs(WIKI_DIR, 0775)

FORM = '''
<p />
<hr />
<form action="%(action)s" method="post">
<textarea name="content" cols="40" rows="10">%(content)s</textarea>
<input type="submit" value="Publish" />
</form>
'''

print "Content-Type: text/html"
print
form = cgi.FieldStorage()
'''
cgi.print_form(form)
cgi.print_environ()
cgi.print_environ_usage()
'''

def fail():
	sys.exit(1)

def do_get():
	query_string = os.getenv('QUERY_STRING')
	if query_string == '':
		path = 'Home'
	else:
		path = query_string.split('&', 1)[0]
	filepath = os.path.join(WIKI_DIR, path)
	if os.path.isfile(filepath):
		contentFile = open(filepath)
		content = contentFile.read()
		print content
	else:
		content = ''
		print '<h1>Page Not Found</h1>'
		print '<h2>Create the page</h2>'
	print FORM % {'action': os.getenv('REQUEST_URI'), 'content': content}


def do_post():
	#cgi.print_form(form)
	#cgi.print_environ()
	query_string = os.getenv('QUERY_STRING')
	if query_string == '':
		path = 'Home'
	else:
		path = query_string.split('&', 1)[0]
	filepath = os.path.join(WIKI_DIR, path)
	content = form.getfirst('content')
	contentFile = open(filepath, 'w')
	contentFile.write(content)
	contentFile.close()
	print content
	print FORM % {'action': os.getenv('REQUEST_URI'), 'content': content}

def do_put():
	do_post()

def do_delete():
	# do the DELETE
	query_string = os.getenv('QUERY_STRING')
	if query_string == '':
		path = 'Home'
	else:
		path = query_string.split('&', 1)[0]
	filepath = os.path.join(WIKI_DIR, path)
	if (os.path.isfile(filepath)):
		os.remove(filepath)
	print '<h1>Page Deleted</h1>'
	print '<h2>' + filepath + '</h2>'

actions = {
		'GET': do_get,
		'POST': do_post,
		'PUT': do_put,
		'DELETE': do_delete,
		}

method = os.getenv('REQUEST_METHOD')
if method == None:
	fail()

print "<html><body>"
actions.get(method.upper(), fail)()
print "</body></html>"

