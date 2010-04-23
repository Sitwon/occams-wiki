#!/usr/bin/env python

import os
import sys
import subprocess
from glob import glob

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

def fail():
	sys.exit(1)

def do_get():
	scriptPath = os.path.join(os.path.split(sys.argv[0])[0], 'output')
	outputScripts = glob(scriptPath + os.path.sep + '*')
	for script in outputScripts:
		if os.path.isfile(script):
			cmd = subprocess.Popen([script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
			outputContent = cmd.communicate('')[0]
	print outputContent

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

	# Pass it to the GET handler to do output
	do_get()

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

if (len(sys.argv) > 1) and (sys.argv[1].lower() == '-pull'):
	scriptPath = os.path.join(os.path.split(sys.argv[0])[0], 'backend')
	backendScripts = glob(scriptPath + os.path.sep + '*')
	for script in backendScripts:
		if os.path.isfile(script):
			backendCmd = subprocess.Popen([script], stdout=subprocess.PIPE)
			content = backendCmd.communicate()[0]
			break
	sys.stdout.write(content)
else:
	print "Content-Type: text/html"
	print
	form = cgi.FieldStorage()

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

