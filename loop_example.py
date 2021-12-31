numbers = [1, 2, 3, 4, 5, 6]

sum = 0

for number in numbers:
  sum = sum + number
  print('element: ', number, ', sum: ', sum)

print(sum)

answer = 1
for number in numbers:
  answer = answer * number
  print('element: ', number, ', answer =', answer)
print(answer)

even_sum = 0

for number in numbers:
  if number % 2 == 0:
    even_sum = even_sum + number
    print('element : ',  number, ', even_sum =', even_sum)
print(even_sum)