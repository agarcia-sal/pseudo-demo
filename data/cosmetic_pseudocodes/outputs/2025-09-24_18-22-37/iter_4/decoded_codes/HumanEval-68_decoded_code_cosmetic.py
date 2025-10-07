from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[int]:
    nodeCount: int = len(array_of_nodes)
    if nodeCount == 0:
        return []

    evens: List[int] = []
    idx: int = 0
    while idx < nodeCount:
        if array_of_nodes[idx] % 2 == 0:
            evens.append(array_of_nodes[idx])
        idx += 1

    if len(evens) == 0:
        return []

    minEven: int = evens[0]
    i: int = 1
    while i < len(evens):
        if evens[i] < minEven:
            minEven = evens[i]
        i += 1

    foundIndex: int = 0
    j: int = 0
    while j < nodeCount:
        if array_of_nodes[j] == minEven:
            foundIndex = j
            break
        j += 1

    return [minEven, foundIndex]