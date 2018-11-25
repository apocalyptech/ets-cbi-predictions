#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import sys
import subprocess

if len(sys.argv) != 2:
    print('Need a number-of-shows-missed count')
    sys.exit(1)
missed = int(sys.argv[1])

# Calculate current points
cur_points_regular = max(0, 100-(10*missed))
cur_points_fancy = max(0, 150-(15*missed))

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
                out.write(line.replace('{{points_regular}}', str(cur_points_regular)).replace('{{points_fancy}}', str(cur_points_fancy)))
print('Wrote to post.bbcode')
