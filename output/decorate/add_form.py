#!/usr/bin/env python

import os
import sys

FORM = '''
<p />
<hr />
<form action="%(action)s" method="post">
<textarea name="content" cols="40" rows="10">%(content)s</textarea>
<input type="submit" value="Publish" />
</form>
'''

content = sys.stdin.read()
print content
print FORM % {'action': os.getenv('REQUEST_URI'), 'content': content}

