# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

my_f = open("hw5.4.txt", "r")
content = my_f.readlines()
my_list = content
my_list_two = ()
loop = 0
loop_two = 0
for element in my_list:
    my_list_two = element.split(" - ")
    my_list[loop] = " - ".join([my_dict.get(my_list_two[0]), my_list_two[1]])
    loop += 1
print(my_list)
for element in my_list:
    print(element)

with open("hw5.4.1.txt", "w") as f_obj:
    while loop_two != loop:
        print(my_list[loop_two], file=f_obj)
        loop_two += 1
