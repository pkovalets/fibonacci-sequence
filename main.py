'''Неделя 1'''
from math import sqrt


def fibonacci(n, k):
    '''
    Возвращает n-е число k-й последовательности Фибоначчи

    :param n:
    Число в последовательности
    :param k:
    Номер последовательности
    '''
    return ((((k + sqrt(k**2 + 4)) / 2)**n + ((k - sqrt(k**2 + 4)) / 2)**n)
            / sqrt(5))


is_running = True
golden_ratio = round((1 + sqrt(5)) / 2, 5)

while is_running:
    user_n = None
    user_k = None
    should_run = None

    while user_n is None or user_n < 0:
        try:
            user_n = int(input('Введите n: '))
        except ValueError:
            print('Число n должно быть целочисленным!')

    while user_k is None or user_k < 0:
        try:
            user_k = int(input('Введите k: '))
        except ValueError:
            print('Число k должно быть целочисленным!')

    try:
        x = fibonacci(user_n, user_k)
        x_prev = fibonacci(user_n - 1, user_k)
        ratio = round(x / x_prev, 5)

        print(f'{user_n}-число {user_k}-й последовательности Фибоначчи: {x}')
        print(f'Отношение числа фибоначчи к предыдущему: {ratio}')

        if ratio > golden_ratio:
            print('Отношение больше золотого сечения')
        elif ratio < golden_ratio:
            print('Отношение меньше золотого сечения')
        else:
            print('Отношение равно золотому сечению')
    except OverflowError:
        print('Результат слишком большой!')
    except ZeroDivisionError:
        print('k не может быть 0!')

    while should_run not in ('y', 'n'):
        should_run = input('Продолжить выполнение программы? (Y/n): ').lower()
        if should_run == 'n':
            is_running = False
        if should_run not in ('y', 'n'):
            print('Неизвестная команда!')
