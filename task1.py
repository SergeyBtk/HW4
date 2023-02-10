import random

counter_list1 = int(input('введите количество элементов 1 списка: '))
counter_list2 = int(input('введите количество элементов 2 списка: '))
my_list1 = [random.randint(0, 20) for i in range(counter_list1)]
my_list2 = [random.randint(0, 20) for i in range(counter_list2)]
new_list = []
print(my_list1)
print(my_list2)
for i in my_list1:
    if i in my_list2:
        new_list.append(i)
for i in my_list2:
    if i in my_list1:
        new_list.append(i)
new_2 = set(new_list)
print(f'повторяющиеся числа в 2-х списках: {(sorted(new_2))}')







