age = int(input("Enter your age: "))
if (age < 0):
  print ("Invalid Age")
elif (age <= 3):
  print ("Baby")
elif (age < 18):
  print ("Kid")
if (age > 100):
  print ("How are you alive?")
elif (age > 60):
  print ("Senior")
else:
  print ("Adult")

print ("Goodbye")