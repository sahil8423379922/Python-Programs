#Check for Voting
name = input("Enter the name")
age =int(input("Enter the Age"))

#Applying the condition
if age>=18:
    print("{} is Eliglible for voting".format(name))
else:
    print("{} is not Eligible for voting".format(name))