# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему
from random import randint
from timeit import timeit
from cProfile import run


def change_max_min_loop(items):
    COUNT_ITEMS = items
    START_ITEMS = -300
    STOP_ITEMS = 300

    my_list = [randint(START_ITEMS, STOP_ITEMS) for x in range(COUNT_ITEMS)]

    max_item_index = 0
    min_item_index = 0

    for n, i in enumerate(my_list):
        if my_list[max_item_index] < i:
            max_item_index = n
        elif my_list[min_item_index] > i:
            min_item_index = n

    my_list[max_item_index], my_list[min_item_index] = my_list[min_item_index], my_list[max_item_index]
    return my_list


print(timeit('change_max_min_loop(400)', number=1000, globals=globals()))  # 0.9384148000000001
print(timeit('change_max_min_loop(1200)', number=1000, globals=globals()))  # 2.5484660000000003
print(timeit('change_max_min_loop(3600)', number=1000, globals=globals()))  # 8.756097200000001

run('change_max_min_loop(400)')
# 1    0.000    0.000    0.002    0.002 task_1.py:19(<listcomp>)
run('change_max_min_loop(1200)')
# 1    0.001    0.001    0.006    0.006 task_1.py:19(<listcomp>)
run('change_max_min_loop(3600)')
# 1    0.002    0.002    0.018    0.018 task_1.py:19(<listcomp>)


def change_max_min_python(items):
    COUNT_ITEMS = items
    START_ITEMS = -300
    STOP_ITEMS = 300

    my_list = [randint(START_ITEMS, STOP_ITEMS) for x in range(COUNT_ITEMS)]

    max_item_index = my_list.index(max(my_list))
    min_item_index = my_list.index(min(my_list))

    my_list[max_item_index], my_list[min_item_index] = my_list[min_item_index], my_list[max_item_index]
    return my_list


print(timeit('change_max_min_python(400)', number=1000, globals=globals()))  # 0.8702572000000011
print(timeit('change_max_min_python(1200)', number=1000, globals=globals()))  # 2.660708099999999
print(timeit('change_max_min_python(3600)', number=1000, globals=globals()))  # 7.949079600000001

run('change_max_min_python(400)')
# 1    0.000    0.000    0.002    0.002 task_1.py:51(<listcomp>
run('change_max_min_python(1200)')
# 1    0.001    0.001    0.006    0.006 task_1.py:51(<listcomp>)
run('change_max_min_python(3600)')
# 1    0.002    0.002    0.017    0.017 task_1.py:51(<listcomp>)


def change_max_min_broken_list(items):
    COUNT_ITEMS = items
    START_ITEMS = -300
    STOP_ITEMS = 300

    my_list = []
    while COUNT_ITEMS != 0:
        my_list.append(randint(START_ITEMS, STOP_ITEMS))
        COUNT_ITEMS -= 1

    max_item_index = 0
    min_item_index = 0

    for n, i in enumerate(my_list):
        if my_list[max_item_index] < i:
            max_item_index = n
        elif my_list[min_item_index] > i:
            min_item_index = n

    my_list[max_item_index], my_list[min_item_index] = my_list[min_item_index], my_list[max_item_index]
    return my_list


print(timeit('change_max_min_broken_list(400)', number=1000, globals=globals()))  # 1.1138088999999987
print(timeit('change_max_min_broken_list(1200)', number=1000, globals=globals()))  # 3.293245299999999
print(timeit('change_max_min_broken_list(3600)', number=1000, globals=globals()))  # 9.374560600000002

run('change_max_min_broken_list(400)')
# 400    0.001    0.000    0.002    0.000 random.py:200(randrange)
# 400    0.000    0.000    0.002    0.000 random.py:244(randint)
# 400    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
# 400    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 400    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
run('change_max_min_broken_list(1200)')
# 1200    0.001    0.000    0.003    0.000 random.py:200(randrange)
# 1200    0.001    0.000    0.004    0.000 random.py:244(randint)
# 1200    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
# 1200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1200    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
run('change_max_min_broken_list(3600)')
# 3600    0.005    0.000    0.011    0.000 random.py:200(randrange)
# 3600    0.003    0.000    0.014    0.000 random.py:244(randint)
# 3600    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
# 3600    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
# 3600    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}


# Вывод:
# * наиболее продуктивным будет решение с использованием функции change_max_min_python, т.к. на
#   выполнение кода уходит меньше времени в том числе из-за использования встроенных функций max() и min());
# * наибольшие затраты по времени идут на генерацию списка my_list, а вчастности на генерацию псевдослучайного числа
#   остальные процессы не столь существенны;
# * при использовании генератора списков время меньше в сравнении с генерацией случайных чисел
#   внутри цикла (в change_max_min_broken_list цикл while) и вставки их в список методом append.
