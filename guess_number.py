# мальчик загадывает число между 1 и 100 (включительно). Компьютер может спросить у мальчика: «Твое число равно, меньше или больше, чем число N?», где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из трёх чисел: 1 — равно, 2 — больше, 3 — меньше.

number_user = int(input('Введите загадываемое число (1-100): '))
a, b = 1, 100
err_txt = 'Ошибка, вы запутались!'

while True:
  n = (a + b) // 2    
  answer = int(input('Твое число равно (1), меньше (3) или больше (2), чем число '+ str(n) + '? '))
  if answer == 2 and n != number_user:
    a = n + 1
    if n == b:
      print (err_txt)
      break
  elif answer == 3 and n != number_user:
    b = n - 1
    if n == a:
      print (err_txt)
      break
  elif n == number_user and answer != 1:
    print ('Вы лжете,')        
    break
  else:    
    break
if n == number_user:
  print ('Ваше число =', n)
elif answer == 1:
  print ('Вы ошиблись, ваше число не равно', n)
