# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на позиции с нечетным индексом.

# 1 Решение

my_list = [2, 3, 5, 9, 5]
sum = 0
for i in my_list:
    if my_list.index(i)% 2 > 0:
        sum += i
        print(sum)


# 2 Решение

from random import randint as ri

my_list = [ri(1, 10) for _ in range(ri(5, 10))]
sum = sum([my_list[i] for i in range(1, len(my_list), 2)])
print(f'Созданный список: {my_list}\nСумма элементов на позиции с нечетным индексом: {sum}')
