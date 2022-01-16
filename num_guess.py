i = 1
while (i <=100):
  print(i)
  i = i + 1
print('End')


is_loop = True
while (is_loop):
  ans = input('Do you want to continue: ')
  if ans =='yes':
    is_loop = True
    print('ans:', ans, 'is_loop:', is_loop)
  else:
    is_loop = False
    print('ans:', ans, 'is_loop:', is_loop)
print('End')