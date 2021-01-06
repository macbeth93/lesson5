# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

# my_f = open("test_hw_5.1.txt", "w")
# my_list = ["string_11\n", "string_22\n", "string_33\n"]
# my_f.writelines(my_list)
# my_f.close()

# my_f = open("test_hw_5.1.txt", "r")
# content = my_f.read()
# print(content)
# my_f.close()

strings = int(input("Введи количество строк, которые отправим в файл:\n>>>"))
print(strings)
my_list = ["string_111\n", "string_221\n", "string_332\n"]
with open("test_hw_5.1.txt", "w") as f_obj:
    while strings != 0:
        print(input("Вводи текст, который отправим в файл:\n>>>"), file=f_obj)
        strings -= 1
    else:
        print("Ты исчерпал свои строчки. Пустая строка.")

with open("test_hw_5.1.txt") as f_obj:
    for line in f_obj:
        print(line)
