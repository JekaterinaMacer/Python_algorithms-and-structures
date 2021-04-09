#8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print('Inter 3 different figures')
a = int(input('Inter the first one'))
b = int(input('Inter the second one'))
c = int(input('Inter the third one'))
if a > b > c or c > b > a:
    print(f'mediana is: {b}')
elif a > c > b or b > c > a:
    print(f'mediana is: {c}')
else:
    print(f'mediana is: {a}')