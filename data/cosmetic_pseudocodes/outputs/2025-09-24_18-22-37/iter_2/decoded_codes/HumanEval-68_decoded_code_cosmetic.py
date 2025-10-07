from typing import List, Union

def pluck(inputNodes: List[int]) -> List[Union[int, int]]:
    nodeCount = len(inputNodes)
    if nodeCount == 0:
        return []

    evens: List[int] = [node for node in inputNodes if node % 2 == 0]

    if not evens:
        return []

    minEven = evens[0]
    for val in evens:
        if val < minEven:
            minEven = val

    idx = 0
    while idx < nodeCount:
        if inputNodes[idx] == minEven:
            break
        idx += 1

    return [minEven, idx]