import sys

print "starting copy"
dfile = sys.argv[1]
data = open(dfile, 'r')

ofile = sys.argv[2]
out = open(ofile, 'w')

copy = data.read()

out.write(line)
data.close
out.close()
