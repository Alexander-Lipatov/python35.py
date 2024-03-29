import contextlib

with contextlib.suppress(ImportError):
    from pyscript import window
    input = window.prompt
    print = window.alert

def main():
  print("Let's compute π:")
  def compute_pi(n):
    pi = 2
    for i in range(1,n):
      pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
    return pi

  pi = compute_pi(100000)
  s = f"π is approximately {pi:.3f}"
  print(s)

main()

print('Hello world', 'sfgdfg\\\'df', 15, sep="\n")
print(0o123)
print(0x53)
print(4==4.)

# Соглашение о именовании констант
DAY_IN_WEEK = 7
print(DAY_IN_WEEK)

a = None
A = 1

print(a, A)
a = 2
print(a)


# Запомните! На основе этого результата можно
# сформулировать следующие правила:
# ■ если аргументы по обе стороны от ** целые числа,
# результат тоже будет целым числом;
# ■ если хотя бы один аргумент ** будет числом с плавающей точкой, результат тоже будет числом
# с плавающей точкой.

print (2e2)
print (2. ** 2)
print (4 ** 0.5)

# int - целое чиcло
# float - чиcло с плавающей точкой

# Деление (результат int только, если оба int)
print(6 * 3) 
# Деление (результат float)
print(6 / 3) 
# Целочисленное деление (откидывает остаток)
print(6 // 3) 
print(7 // 3) 

#! Примечание: некоторые значения являются отрицательными. 
#! Очевидно, это повлияет на результат. Но как?
#! Результат — две отрицательные двойки. Реальный
#! (не округленный) результат -1.5 в обоих случаях. Тем не
#! менее, результаты всегда округляются. Округление идет
#! к меньшему целому значению, а меньшее целочисленное
#! значение — это -2, отсюда: -2 и -2.0.

print(-6 // 4)
print(6. // -4)

# !Операторы: как не делить
# Как вы, наверное, знаете, деление на ноль не работает.
# Не пытайтесь делать следующее:
# ■ делить на ноль;
# ■ делить целое число на ноль;
# ■ находить остаток от деления на ноль.

# Левостороннее связваение
print(9 % 6 % 2)
# Правостороннее связваение
print((2 ** 2) ** 3)


# Примечание. PEP 8 — руководство по коду на Python
# рекомендует следующее соглашение об именовании
# переменных и функций в Python:
# ■ Имена функций должны состоять из маленьких
# букв, а слова разделяться символами подчеркивания — это необходимо, чтобы их было легче
# прочитать (например, var, my_variable).
# ■ Имена функций соблюдают те же правила, что
# и имена переменных (например, fun, my_function).
# ■ Стиль mixedCase (смешанный регистр, например, myVariable) допускается в тех местах, где
# уже преобладает такой стиль, для сохранения
# обратной совместимости.

print(len(['False', 'None', 'True', 'and', 'as', 'assert',
'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try',
'while', 'with', 'yield']))

print("Python version: " + str(3))
print(15 + int('3'))
print(15 + float('3'))
print(15 + bool('3'))
print(15 + bool(''))
print(15 + bool(0))

var = 1
var +=1
var -=1
print(var)
print(27**(1/3))

# inp = int(input('Введи число\n'))
# print(inp)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


print(bool("")) 
print(bool(0.0))
print(bool(None))
print(bool("IT Step Academy"))
print(bool(1)) 
print(bool({})) 
print(bool([])) 
print(1 and 8 and 0) 
print(0 or '' or 8 or []) 

car_speed = 100
if 50 < car_speed < 150:
  print("Car is faster than 50 km/h")
elif car_speed == 100:
  print('"---"')
else:
  print('moto')
  
try:
  1/0
except ValueError:
  print("Improper value was obtained")
except Exception as ex:
  print("Hmm... Something went wrong", ex)

# while True:
#   try:
#     apples = int(input("Enter the amount of apples you have: "))
#     if apples < 0:
#       raise Exception("You can’t have -10 apples")
#     parts_number = int(input("Enter the number of parts:"))
#     parts_amount = apples / parts_number
#     print("You have " + str(apples) + " apples \n")
#     print("Each of " + str(parts_number) +
#     " parts consists of " +
#     str(parts_amount) + " apples")
#   except (ZeroDivisionError, ValueError):
#     print("Improper value was obtained")
#   except Exception as ex:
#     print(ex)
#   except:
#     print("Hmm... Something went wrong")


number = 0
while number < 300:
  number += 1
  if number % 3 != 0:
    continue
  elif number % 5 != 0:
    print(number, "divides by 3")
  elif number % 7 != 0:
    print(number, "divides by 3 and 5")
  else:
    print(number, "divides by 3 and 5 and 7")
    
def SumOrMul(event):
  nums = input('3 num split space').split(' ')
  operation = input('operation type (* or +)')
  total = 0

  if operation == '*':
    total = 1

  for n in nums:
    if operation == '+':
      total+=int(n)
    else:
      total*=int(n)
      
  if operation == '+':
    print('sum is', total)
  else:
    print('mul is', total)
    