import functools

def validate(card_number):
  card_number_string = str(card_number)
  card_num = []
  for idx, n in enumerate(card_number_string):
    n_int = int(n)
    if (idx + 1)% 2 == 0:
      multiply_num = n_int*2
      number = 0
      if multiply_num >= 10:
        for i in str(multiply_num):
          print(i)
          number += int(i)
        print(number, n_int)
        card_num.append(number)
    else:
      card_num.append(n_int)
  sum_card_num = functools.reduce(lambda x,y : x + y, card_num)
  print(sum_card_num)
  return True