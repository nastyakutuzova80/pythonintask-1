# Задача 4. Вариант 16.
# Напишите программу, которая выводит имя, под которым скрывается Мартин Андерсен. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.
# Udovenko A. Y.
# 28.02.2017
prof = "писатель-коммунист"
ln = "Андерсен"
b = int (1869)	
d = int (1954)
t = "Копенгаген"
print ("\t\t\tМинутка Википедии в Python!\nМартин Андерсен-Нексе — известный датский", prof,"и один из основателей Коммунистической партии Дании.")
print ("Hастоящая фамилия -", ln)
print ("Oн родился в", b,"в городе", t, ", a умер в", d,"в возрасте", d-b, "лет.")
input ("\nНажмите Enter, чтобы выйти")
