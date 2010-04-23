#!/usr/bin/env python

import os
import sys
import subprocess
from glob import glob

import cgitb
cgitb.enable()

conductor = os.getenv('SCRIPT_FILENAME')
conductorCmd = subprocess.Popen([conductor, '-pull'], stdout=subprocess.PIPE)
content = conductorCmd.communicate()[0]
if content == '':
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
