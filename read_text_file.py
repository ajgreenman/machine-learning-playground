"Read and display a text file"

FNAME = raw_input("Enter filename: ")
print

try:
    FOBJ = open(FNAME, 'r')
except IOError, exc:
    print "*** file open error:", exc
else:
    for eachLine in FOBJ:
        print eachLine,
    FOBJ.close()

print
