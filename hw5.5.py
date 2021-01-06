# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("hw_5.5.txt", "w") as f_obj:
    print(input("Вводи число через запятую:\n>>>"), file=f_obj)
answer = 0
loop = 0
with open("hw_5.5.txt", "r") as f_obj:
    content = f_obj.read()
    print("content = ", type(content))
    my_list = content.split(",")
    print("my_list", my_list)
    for element in my_list:
        answer = answer + int(element)

print("Сумма равна:", answer)
