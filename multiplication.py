for i in range (1,10):  # outer loop
  print('i:', i)
  for j in range(1,5):  # inner loop
    print('i:', i, 'j:', j)

for f in range(1, 11):
  for k in range(1, 13):
    answer = f * k
    print(f, 'x', k, '=', answer)
  print('______________')