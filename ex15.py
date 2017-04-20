from sys import argv

script, filename = argv

txt = open(filename)

print "File : %r:" % filename
print txt.read()

print "Type another file:"
file2 = raw_input(">")

txt2 = open(file2)

print txt2.read()

