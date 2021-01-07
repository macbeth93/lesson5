# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_f = open("hw5.2.txt", "r")
content = my_f.readlines()
# content = int(content)
print("Число строк", len(content))
print(content)
element_list = ()

for element in content:
    element_list = element.split(" ")
    print(len(element_list))
