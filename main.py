x = True
print (x)
print (type(x))
y = 5 != 5
print("Value of y is", y)


def add(addend1, addend2):
  print('adding', addend1, 'and', addend2)
  return addend1+ addend2;

a = add(1, 2)
print(a)

def division(dividend, divisor):
  print('dividing', dividend, 'and',  divisor)
  quotient = dividend/ divisor
  return quotient

d = division(15, 3)
print (d)

def subtract(s1,s2):
  print ('subtracting', s1, 'and', s2)
  return s1- s2

s = subtract (10, 5)
print (s)

def multiply(m1, m2):
  print('multipling', m1, 'and', m2)
  return m1* m2

m = multiply (4, 2)
print (m)