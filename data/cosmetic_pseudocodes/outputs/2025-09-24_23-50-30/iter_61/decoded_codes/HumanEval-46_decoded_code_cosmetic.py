from typing import List


def fib4(integer_n: int) -> int:
    resultsList: List[int] = [0, 0, 2, 0]

    if integer_n == 0:
        return resultsList[0]
    elif integer_n == 1:
        return resultsList[1]
    elif integer_n == 2:
        return resultsList[2]
    elif integer_n == 3:
        return resultsList[3]
    else:
        return computeTail(resultsList, 4, integer_n)


def computeTail(activeList: List[int], index_x: int, limit_y: int) -> int:
    if index_x <= limit_y:
        sum_val = sum(activeList)
        # Advance the list window and recurse
        activeList = activeList[1:4] + [sum_val]
        return computeTail(activeList, index_x + 1, limit_y)
    else:
        return activeList[3]