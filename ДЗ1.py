a = input('Введите текст: ')
print(a);

b= input('Введите текст из 3-х слов: ')
print(b)
b1= b.replace (' ', '!')
print (b1);

c = 'Информатика'
print(c);
c1 = c[2:7]
c1 = c1.capitalize ()
c2 = c[1] + c[3:7]
c2 = c2.capitalize ()
c3 = c[7] + c[6] + c[9] + c[7:11]
c3 = c3.capitalize ()
print (c1);
print (c2);
print (c3);

d = input('Введите первое число: ')
d = float(d)
d1 = input('Введите второе число: ')
d1 = float(d1)
d2 = input('Введите третье число: ')
d2 = float(d2)
s = (d + d1 + d2)**float(2)
s = str(s)
print ('Квадрат суммы чисел: ' + s);
r = (d - d1 - d2)**float(2)
r = str(r)
print ('Квадрат разности чисел: ' + r);

