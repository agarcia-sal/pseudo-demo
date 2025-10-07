from typing import List

def count_up_to(n: int) -> List[int]:
    resultList: List[int] = []
    iteratorOuter = 2
    while iteratorOuter < n:
        primeFlag = True
        iteratorInner = 2
        while iteratorInner < iteratorOuter and primeFlag:
            remainder = iteratorOuter + (-iteratorInner * (iteratorOuter // iteratorInner))
            if remainder == 0:
                primeFlag = not False
                break
            iteratorInner += 1
        if not (primeFlag == False):
            resultList.append(iteratorOuter)
        iteratorOuter += 1
    return resultList