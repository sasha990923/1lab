
# уровень а
#№1
a = int(input("введите ваш возраст: "))
if a >= 18:
    print("вы можете голосовать")
else:
    print("вам пока нельзя голосовать")
#№2
name = "саша"
print(f"Привет,{name}")
#№3
b = int(input("введите число: "))
if b % 2 == 0:
    print("четное число")
else:
    print("нечетное число")
#№4
grade = int(input("оченка ученика от 1 до 5"))
if grade == 5:
    print("отлично")
else:
    print("оцнка принета")
#№5
z = int(input("введите первое число: "))
x = int(input("введите второе число: "))
if z > x:
    print("первое число больше")
elif z < x:
    print("второе число больше")
else:
    print("ошибка")
#№6
porol = input("ввдедите пороль из 6 символов: ")
if len(porol) == 6:
    print("пороль принят")
else:
    print("ваш пороль слишком короткий")
#№7
w = str(input("введите слово: "))
if 'a' in w:
    print("буква a найдена")
else:
    print("нет буквы a")
#№8
r = int(input("введите что-то: "))
print(type(r))
if type(r) == int:
    print("это число")
elif type(r) == str:
    print("это cтрочное")
elif type(r) == float:
    print("это не целое")
elif type(r) == bool:
    print("это булевое значение")
else:
    print("ошибка")
# уровень в
#№1
p = int(input("введите первое целое число: "))
u = int(input("введите второе целое число: "))
q = int(input("введите третие целое число: "))
if p > u and p > q:
    print(f"самое большое число:{p}")
elif u > p and u > q:
    print(f"самое большое число:{u}")
elif q > p and q > u:
    print(f"самое большое число:{q}")
else:
    print("ошибка")
#№2
d = int(input("введите сторону квадрата: "))
S = d*d
if d <= 0:
    print("ошибка")
else:
    print(S)
#№3
X = float(input("введите кардинату X: "))
Y = float(input("введите кардинату Y: "))
if X > 0 and Y > 0:
    print("точка находится в первой четверти")
elif X < 0 and Y > 0:
    print("точка находится во второй четверти")
else:
    print("точка не принадлежит первой или второй четверти")
#№5
e = int(input("введите цену товара"))
if e >= 100:
    t = e - e * 0.1
    print(t)
else:
    print(f"скидки нет, сумма товара = {e}")
#№6
h = int(input("ведите число каторое делиться на 3 и на 5: "))
if h/3 and h/5:
    print("делиться оба числа")
else:
    print("не деляться на оба числа")
#№7
k = int(input("введите номер месеца: "))
if 1 and 2 and 12:
    print("это зима")
elif 3 and 4 and 5:
    print("это весна")
elif 6 and 7 and 8:
    print("это лето")
elif 9 and 10 and 11:
    print("это осень")
else:
    print("такого месеца нету")

#№8
j = int(input("введите свое рост в см: "))
if j < 150:
    print("низкий")
elif 150 <= j and j <= 175:
    print("средний")
else:
    print("высокий")
