from typing import List

def fib4(integer_n: int) -> int:
    tempList: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return tempList[integer_n]

    currentIndex: int = 4
    while currentIndex <= integer_n:
        nextTerm = tempList[3] + tempList[2] + tempList[1] + tempList[0]
        tempList.append(nextTerm)
        del tempList[0]
        currentIndex += 1

    return tempList[3]