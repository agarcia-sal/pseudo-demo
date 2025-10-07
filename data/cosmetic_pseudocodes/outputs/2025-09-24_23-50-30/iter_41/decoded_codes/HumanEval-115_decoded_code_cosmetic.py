from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    index: int = 0
    acc: int = 0
    data: List[List[int]] = grid
    n: int = len(data)
    while index < n:
        tempSum: int = 0
        pos: int = 0
        row: List[int] = data[index]
        m: int = len(row)
        while True:
            if pos >= m:
                break
            tempSum += row[pos]
            pos += 1
        acc += ceil(tempSum / capacity)
        index += 1
    return acc