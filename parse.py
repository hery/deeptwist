"""
    This script removes all non-image requests from our curl script.
    Alternatively, we could remove all non-graphql requests in a script that chains graphql
    requests with a higher image fetch limit, and chain end_cursor as after parameters.

    This should be a global script that traverses every class in data, e.g:        
        * data/adhomukhasvanasana/curl.sh
        * data/bakasana/curl.sh

    Then curl all images into e.g.:
        * data/adhomukhasvanasana/
        * data/bakasana/
"""

FILEPATH = 'curl.sh'
lines = None

with open(FILEPATH, 'r') as fp:
    lines = fp.readlines()
    print('read %s lines' % len(lines))
    fp.close()

with open(FILEPATH, 'w') as fp:
    for line in lines:
        if 'https://scontent-lhr3-1.cdninstagram.com/vp' in line:
            line = line.replace('curl', 'curl -O') # -O preserves the original name
            fp.write(line)
    fp.close()
