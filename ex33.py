i = 0
numbers = []

while i < 6:
  print "At the top i is %d" %i #Why am I not just skipping this lesson?
  numbers.append(i)

  i+= 1

  print "Numbers now: ", numbers
  print "At the bottom, i is %d" % i

print "The Numbers:"
for num in numbers:
  print num
