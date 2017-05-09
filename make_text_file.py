"Makes a text file based on user input."

import os

while True:
    FNAME = raw_input("Enter file name: ")
    if os.path.exists(fname):
        print "Error: '%s' already exists" % FNAME
    else:
        break

ALL = []
print "\nEnter lines ('.' by itself to quit).\n"

while True:
    ENTRY = raw_input('> ')
    if ENTRY == '.':
        break
    else:
        ALL.append(ENTRY)

FOBJ = open(FNAME, 'w')
FOBJ.write('\n'.join(ALL))
FOBJ.close()

print 'Done!'
