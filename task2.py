# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9
from random import randint

trees = int(input('Введите количество кустов на грядке: '))
trees_berry = []
for i in range(trees):
    berry_random = randint(1, 20)
    trees_berry.append(berry_random)
print(f'Колличество ягод на каждом кусте: {trees_berry}')

sum_berry = []
for i in range(trees):
    if i == 0:
        x1 = trees_berry[i]
        x2 = trees_berry[i + 1]
        x3 = trees_berry[-1]
        sum1 = x1 + x2 + x3
        sum_berry.append(sum1)
        # print(f'первый параметр {x1 + x2 + x3}')
    elif i == trees - 1:
        x1 = trees_berry[i]
        x2 = trees_berry[0]
        x3 = trees_berry[i-1]
        sum2 = x1 + x2 + x3
        sum_berry.append(sum2)
        # print(f'последний параметр {x1 + x2 + x3}')
    elif i != 0 or i != trees - 1:
        x1 = trees_berry[i]
        x2 = trees_berry[i + 1]
        x3 = trees_berry[i - 1]
        sum3 = x1 + x2 + x3
        sum_berry.append(sum3)
        # print(f'все числа {x1 + x2 + x3}')
print(f'список количества ягод с 3-х соседних кустов: {sum_berry} \n')
print(f'Максимальное количество ягод которое можно собрать за 1 заход: {max(sum_berry)}')