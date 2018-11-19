#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import subprocess

# Get score output
score_text = subprocess.run(
        ['./scores.py'],
        capture_output=True,
        text=True,
        ).stdout

with open('post.bbcode.in', 'r') as df:
    with open('post.bbcode', 'w') as out:
        for line in df.readlines():
            if line.strip() == '{{scores}}':
                out.write(score_text)
            else:
                out.write(line)
print('Wrote to post.bbcode')
