a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
if a==b:
    print('Число a равно числу b')
else:
    print('Число a не равно числу b')

    
a = int(input('Введите целое число: '))
b = a%2
if b==0:
    print ('Введенное число кратно 2')
else:
    print ('Введенное число не кратно 2');


a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))
if a>b:
    if a>c:
        a = str(a)
        print ('Наибольшее число: ' + a)
    else:
        c = str(c)
        print ('Наибольшее число: ' + c)
elif b>c:
    b = str(b)
    print('Наибольшее чисо: ' + b)
else:
    c = str(c)
    print ('Наибольшее число: ' + c)
    
    
a = [9, 6, 10, 13, 1]
spisok1 = sorted(a)
long = len(a)
print (spisok1)
print (long)


a = [8, 3, 1, 1, 9, 1]
kol1=a.count(1)
print(kol1)
kratn = kol1%3
if kratn == 0:
    print('Количество единиц кратно трем')
else:
   print('Количество единиц не кратно трем')
   
def uravnenie (x,y,z):
    return x**2-z*x+5*z - y
lowerBound = int(input("Введите нижнюю границу поиска решений:"))
upperBound = int(input("Введите верхнюю границу поиска решений: "))
for x in range(lowerBound, upperBound):
    for y in range(lowerBound, upperBound):
        for z in range(lowerBound, upperBound):
            if (uravnenie(x, y, z)):
                print("x=",x, end = ", ")
                print("y=", y, end = ", ")
                print("z=",z, end = "; " )
                a = datetime.today()
                print(a)
                
a = [] 
for i in range(0, 5):
    a.append(input('Введите ' + str(i) + ' элемент списка: '))
print(a)
a1 = a
a1.pop(0)
print(a1)

