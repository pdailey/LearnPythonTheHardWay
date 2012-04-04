from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)"
print "Otherwise, hit return."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
print "I'm going to write these to the file."
for x in range(0,3):
  line = raw_input("> ")
  target.write(line + "\n")

print "And finally, we close the file."
target.close()

