# This is like one of the argv scripts
def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
  print "arg1: %r" % arg1

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")

