#7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
print('whether the year is a leap')
a = int(input('Inter a year'))
if (a % 4==0 and a % 100 !=0) or (a % 400==0):
    print('the year is a leap')
else:
    print('the year is a non-leap')