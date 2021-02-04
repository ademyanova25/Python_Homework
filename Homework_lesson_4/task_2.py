# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randrange


def generator(lst):
    lst_new = []
    for i in range(len(lst)-1):
        if lst[i + 1] > lst[i]:
            lst_new.append(lst[i + 1])
    return lst_new


lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(lst)
print(generator(lst))

lst = [randrange(1, 250, 1) for i in range(10)]
print(lst)
print(generator(lst))
