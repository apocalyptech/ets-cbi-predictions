#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import sys
import subprocess

if len(sys.argv) != 2:
    print('Need a number-of-shows-missed count')
    sys.exit(1)
missed = int(sys.argv[1])

# Calculate no-debut vote points
points_no_debut = max(0, 100-(10*missed))

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
                out.write(line.replace('{{points_no_debut}}', str(points_no_debut)))
print('Wrote to post.bbcode')
