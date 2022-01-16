print('Think of a number in between 1 and 100.')
print()
start = 1
end = 100
ans_not_found = True

while (ans_not_found == True):
  avg = int((start + end) / 2)
  print('start =', start, 'end =', end, 'avg =', avg, 'ans_not_found =', ans_not_found)
  if start == end:
    print('You guessed', start)
    ans_not_found = False
  elif (start + 1 == end):
    response = int(input('Enter 1 if it is ' + str(start) + ', otherwise enter 2: '))
    if response == 1:
      print('You guessed', start)
      ans_not_found = False
    else:
      print('You guessed', end)
      ans_not_found = False
  else:
    response = int(input('Enter 1 if it is <= ' + str(avg) + ', 2 if it is > ' + str(avg) + ': '))
    if response == 1:
      end = avg
      start = start
    else:
      start = avg + 1
      end = end
print('End')