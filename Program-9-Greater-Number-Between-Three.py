#Greater Between three
a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=int(input("Enter Third Number"))

if a>b:
  if a>c:
    print("{} is the Greater Number".format(a))
  else:
    print("{} is the Greater Number".format(c))
else:
  if b>c:
    print("{} is the Greater Number".format(b))
  else:
    print("{} is the Greater Number".format(c))


  