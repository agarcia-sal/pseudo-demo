from typing import List

def fib4(counter: int) -> int:
    tempList: List[int] = [0, 0, 2, 0]

    def recur(index: int) -> int:
        if index < 4:
            return tempList[index]
        aggregated = sum(tempList)
        tempList.pop(0)  # Remove first element
        tempList.append(aggregated)
        return recur(index - 1)

    return recur(counter)