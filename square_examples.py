for i in range(1,5):
  for k in range(1,5):
    print('x ', end='')
  print('')

print('-----------------------------')

num = int(input('Please enter the total number of rows: '))

for f in range(1, num + 1):
  for j in range(1, f + 1):
    print('X', end=' ')
  print()

print('-----------------------------')

for f in range(1, num + 1):
  for j in range(1, num + 1):
    if(j >= f):
      print('X', end=' ')
print()