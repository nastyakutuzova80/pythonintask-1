# Задача 7. Вариант 16.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой
# игрок получал бы большее количество баллов за меньшее количество попыток.

# Смирнов Н.Н.
# 15.03.2017

import random

names = "Анастасия Романовна Захарьина-Юрьева","Мария Темрюковна","Марфа Васильевна Собакина",\
       "Анна Алексеевна Колтовская","Анна Григорьевна Васильчикова","Мария Фёдоровна Нагая"
score = 0
attempts = 1
end_score = 0

print("Компьютер загадал случайное имя одной из шести жён Ивана IV Грозного")
print("Список возможных вариантов ответа: ", names)

yeah = "нет"
while yeah == "нет":
    random_pc_name = names[random.randint(0, 5)]
    answer_player = input("Введите Ваш ответ: \n")
    if answer_player == random_pc_name:
        print("Верно! ", random_pc_name)
        score += 10
        yeah = "да"
    else:
        print("\nСожалею, но вы ошиблись.")
        print("Попробуем снова!")
        attempts += 1

print ("Игра окончена.")
end_score = score // attempts
print ("Ваш счёт: " + str(end_score) + " очка(очков).")
