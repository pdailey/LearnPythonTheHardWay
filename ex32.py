the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This kind of for loop goes through a list
for number in the_count:
  print "This is count %d" % number

# same as above
for fruit in fruits:
  print "A fruit of type: %s" % fruit

# We can go through a mixed list too
# note that %r is used because we don't know what is in it
for i in change:
  print "I got %r" % i

# We can also build lists.
# first start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
for i in range (0, 6):
  print "Adding %d to the list." %i
  # Append id a function that lists understand.
  elements.append(i)
  # Now we print them out too
  print "Element was: %d" % i
