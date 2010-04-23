#!/usr/bin/env python

import os
import sys
import subprocess
from glob import glob

import cgitb
cgitb.enable()

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
	print '<h1>Page Not Found</h1>'
	print '<h2>Create the page</h2>'

#print FORM % {'action': os.getenv('REQUEST_URI'), 'content': content}

# Pass content to the Render Engine
renderedContent = content
scriptPath = os.path.join(os.path.split(sys.argv[0])[0], 'render')
renderScripts = glob(scriptPath + os.path.sep + '*')
for script in renderScripts:
	if os.path.isfile(script):
		renderCmd = subprocess.Popen([script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		renderedContent = renderCmd.communicate(renderedContent+'\n')[0]

# Pass content to the Decorate Engine
decoratedContent = renderedContent
scriptPath = os.path.join(os.path.split(sys.argv[0])[0], 'decorate')
decorateScripts = glob(scriptPath + os.path.sep + '*')
for script in decorateScripts:
	if os.path.isfile(script):
		decorateCmd = subprocess.Popen([script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		decoratedContent = decorateCmd.communicate(decoratedContent+'\n')[0]

print decoratedContent
