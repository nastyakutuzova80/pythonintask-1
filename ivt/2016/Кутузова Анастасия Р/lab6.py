#Задача 6. Вариант 9.
#Создайте игру, в которой компьютер загадывает имя одного из трех поросят, а игрок должен его угадать.
import random
print('Я загадал одного из трёх поросят.')
name = input('Попробуй угадать')
pig = random.randint(1,3)
if pig == 1:
	guessed = 'Ниф-Ниф'
elif pig == 2:
	guessed = 'Наф-Наф'
elif pig == 3:
	guessed = 'Нуф-Нуф'
if name == guessed:
	print('Верно,ты угадал"')
else:
	print('Неверно')
input ('Нажмите Enter для выхода')
