# ������� ���������� ����� ����� 1 � 100 (������������). ��������� ����� �������� � ��������: ����� ����� �����, ������ ��� ������, ��� ����� N?�, ��� N � �����, ������� ����� ��������� ���������. ������� �������� ����� �� ��� �����: 1 � �����, 2 � ������, 3 � ������.

number_user = int(input('������� ������������ ����� (1-100): '))
a, b = 1, 100
err_txt = '������, �� ����������!'

while True:
  n = (a + b) // 2    
  answer = int(input('���� ����� ����� (1), ������ (3) ��� ������ (2), ��� ����� '+ str(n) + '? '))
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
    print ('�� �����,')        
    break
  else:    
    break
if n == number_user:
  print ('���� ����� =', n)
elif answer == 1:
  print ('Вы ошиблись, ваше число не равно', n)
