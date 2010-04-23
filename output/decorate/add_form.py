#!/usr/bin/env python

import os
import sys
import subprocess

import cgitb
cgitb.enable()

FORM = '''
<p />
<hr />
<form action="%(action)s" method="post">
<textarea name="content" cols="40" rows="10">%(content)s</textarea>
<input type="submit" value="Publish" />
</form>
'''

renderedContent = sys.stdin.read()
print renderedContent

conductor = os.getenv('SCRIPT_FILENAME')
conductorCmd = subprocess.Popen([conductor, '-pull'], stdout=subprocess.PIPE)
content = conductorCmd.communicate()[0]
print FORM % {'action': os.getenv('REQUEST_URI'), 'content': content}

