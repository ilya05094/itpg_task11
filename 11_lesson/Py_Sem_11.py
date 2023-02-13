# -*- coding: utf-8 -*-

# -- Sheet --

from sympy import *
from sympy.plotting import plot

x = Symbol("x")
f = 5 * x ** 2 + 10 * x - 30
f

# 1. Определить корни
#    Нули функции

solveset(f, x)

# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# https://poznayka.org/s79613t1.html

f_diff = [-oo, oo] 
f_diff[1:1] = solve(diff(f), x)

incr_list = []
decr_list = []

for i in range(1, len(f_diff)):
    val = is_increasing(f, Interval.open(f_diff[i - 1], f_diff[i]))
    if val:
        incr_list.append(f"[{f_diff[i - 1]}, {f_diff[i]}]")
    else:
        decr_list.append(f"[{f_diff[i - 1]}, {f_diff[i]}]")

print(f"Убывает на интервалах:", *decr_list, sep="\n")
print(f"Возрастает на интервалах:", *incr_list, sep="\n")

    # 4. Построить график

plot(f, (x, -5, 2.5), legend=True)

# 5. Вычислить вершину
#    Экстремумы функции

ext_list = solve(diff(f), x)

for i in ext_list:
    res = f.subs(x, i)
    if res < 0:
        print(f"Точка минимума: (x:{i}, y:{res})")
    elif res > 0:
        print(f"Точка максимума: (x:{i}, y:{res})")

# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
#    Знакопостоянства функции
#    https://openvorkuta.ru/chto-takoe-promezhutki-zakona-postoianstva

roots_fun = [-oo, oo]
roots_fun[1:1] = solve(f, x)

incr_list = []
decr_list = []

for i in range(1, len(roots_fun)):
    num_1, num_2 = roots_fun[i - 1], roots_fun[i]
    val = is_increasing(f, Interval.open(num_1, num_2))
    if val:
        incr_list.append(f"[{num_1}, {num_2}]")
    else:
        decr_list.append(f"[{num_1}, {num_2}]")

print("f > 0:", *incr_list, sep="\n")
print("f < 0:", *decr_list, sep="\n")

