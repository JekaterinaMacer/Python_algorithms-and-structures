#5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
print('what letter is it')
n = int(input('Inter the number'))
n = ord('a') + n - 1
print(f'the letter is {chr(n)}')
