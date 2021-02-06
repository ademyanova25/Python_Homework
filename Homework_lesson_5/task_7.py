# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('for_task_7.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    d = {}
    d_average_profit = {}
    lst = []
    average_profit_lst = []
    for line in lines:
        firm, o, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profit_lst.append(profit)
        d[firm] = profit
        average_profit = sum(average_profit_lst) / len(average_profit_lst)
        d_average_profit['average_profit'] = average_profit
        lst = d, d_average_profit
    with open('for_task_7_json.txt', 'w', encoding='utf-8') as f_2: # Не поняла нужно ли сохранять в новый файл или в этот же. Решила в новый
        json.dump(lst, f_2)

