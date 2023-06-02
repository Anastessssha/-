# Бессонова Анастасия 44-22-122 задание 1
import math
import sys


def main(*args):
    try:
        x = float(args[0][0])
        if x < 0:
            return math.log10(math.sqrt(x ** 2 + 3.44))
        else:
            return math.sqrt(x ** 2 - 0.48 * x)
    except:
        return "Произошла ошибка"

print(main(sys.argv[1:]))