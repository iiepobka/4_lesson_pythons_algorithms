# 2). Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и
# сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
from timeit import timeit
from cProfile import run

def sieve(number):
    go_to = number  # int(input('Введите цифрой номер i-го по счёту простого числа, которое надо вывести: '))

    result = []
    n = 3
    count = 1

    while len(result) < go_to:
        result.clear()

        a = [0] * n

        for i in range(n):
            a[i] = i

        a[1] = 0
        m = 2

        while m < n:
            if a[m] != 0:
                j = m * 2
                while j < n:
                    a[j] = 0
                    j = j + m
            m += 1

        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])

        del a

        n += count
        count += 1
        result += b

    return f'{go_to}-е по счету простое число: {result[go_to - 1]}'

print(timeit('sieve(10)', number=1000, globals=globals()))  # 0.0725481
print(timeit('sieve(30)', number=1000, globals=globals()))  # 0.46659110000000004
print(timeit('sieve(90)', number=1000, globals=globals()))  # 3.5001721

run('sieve(10)')
#         9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        41    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         8    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
run('sieve(30)')
#        17    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       207    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        16    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
run('sieve(90)')
#        32    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1098    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        31    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}

def prime(number):
    go_to = number  # int(input('Введите цифрой номер i-го по счёту простого числа, которое надо вывести: '))
    result = []
    START = 2

    while len(result) != go_to:
        if START == 2:
            result.append(START)

        for i in result:
            if START % i == 0:
                break
            elif i == result[-1]:
                result.append(START)
                break
        START += 1

    return f'{go_to}-е по счету простое число: {result[go_to - 1]}'

print(timeit('prime(10)', number=1000, globals=globals()))  # 0.020820300000000458
print(timeit('prime(30)', number=1000, globals=globals()))  # 0.1217706999999999
print(timeit('prime(90)', number=1000, globals=globals()))  # 0.9923090999999999

run('prime(10)')
#        29    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
run('prime(30)')
#       113    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        30    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
run('prime(90)')
#       463    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        90    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}s}

# Более сложный и более мендленный оказался алгоритм sieve, т.к. использует больше
# различных методов и их вызовов для выполнения поставленной задачи.
