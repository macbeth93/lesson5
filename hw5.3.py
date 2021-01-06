# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# File:
# Znajka
# 250000
# Vorchun
# 15000
# Molchun
# 22000
# Toropyzhka
# 10000
# Rasteryajka
# 5000

# ДЛЯ ПРЕПОДА. Я перевёл строчки из файла в ключи и наполнитель в списки. Из двух списков сделал словарь ну и по нему
# уже анализировал. Как-то громоздко, но я хотел попрактиковаться еще со словарём и генератором.

my_f = open("hw5.3.txt", "r")
content = my_f.readlines()
print("Число строк:", len(content))
my_f.close()

my_f = open("hw5.3.txt", "r")
my_list = my_f.read().split('\n')
keys = [el for el in my_list if el.isdigit()]
for element in my_list:
    if element.isdigit():
        my_list.remove(element)
values = [element for element in my_list]
salaries_count = len(keys)
salaries_summaries = 0
for element in keys:
    element = int(element)
    salaries_summaries = salaries_summaries + element
print("Средняя зарплата:", salaries_summaries / salaries_count)
dicts = dict(zip(keys, values))
# print("Keys:", keys)

for keys in dicts:
    keys = int(keys)
    if keys < 20000:
        keys = str(keys)
        print(dicts.get(keys), "получил больше 20 тысяч")

