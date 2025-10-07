from typing import List

def factorize(param_x: int) -> List[int]:
    resultList: List[int] = []
    currentDiv: int = 2
    limit: float = param_x ** 0.5 + 1
    while currentDiv <= limit:
        if param_x % currentDiv == 0:
            resultList.append(currentDiv)
            param_x //= currentDiv
            limit = param_x ** 0.5 + 1
        else:
            currentDiv += 1
    if param_x > 1:
        resultList.append(param_x)
    return resultList