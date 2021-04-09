#4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
print('Inter 2 different letters')
a = ord(input('Inter the first one'))
b = ord(input('Inter the second one'))
aa = a - ord('a') + 1
bb = b - ord('a') + 1
print(f'index number for {chr(a)} is: {aa}')
print(f'index number for {chr(b)} is: {bb}')
print(f'between them {abs(a-b)-1} letters')