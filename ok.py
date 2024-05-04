from typing import List


def rob(data: List[int]) -> int | None:
    res = [None] * len(data) # заполняем список чтобы было удобно обратиться по индексу
    res[0] = data[0] # заполняем список первыми двумя элементами т.к. эти элементы вместе итак не рассматриваем
    res[1] = data[1]

    for pos in range(2, len(data)): # запускаем цикл без учета двух первых элементов
        res[pos] = (max(data[pos] + res[pos - 2], res[pos - 1])) # max(сумма нынешнего элемента и предыдущего через 2, просто записываем то что есть)
    return res[-1]


d = [1, 2, 3, 4, 5, 6]
print(rob(d))
