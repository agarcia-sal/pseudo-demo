from typing import List

def minPath(array: List[List[int]], delta: int) -> List[int]:
    n = len(array)
    epsilon = n * n + 1

    def traverse(x: int, y: int) -> List[int]:
        if x < 0 or y < 0 or x >= n or y >= n:
            return []
        return [array[x][y]]

    indexA = 0
    while indexA < n:
        indexB = 0
        while indexB < n:
            if array[indexA][indexB] == 1:
                collector: List[int] = []
                if indexA != 0:
                    collector += traverse(indexA - 1, indexB)
                if indexB != 0:
                    collector += traverse(indexA, indexB - 1)
                if indexA != n - 1:
                    collector += traverse(indexA + 1, indexB)
                if indexB != n - 1:
                    collector += traverse(indexA, indexB + 1)

                if collector:
                    minVal = collector[0]
                    for counter in range(1, len(collector)):
                        if collector[counter] < minVal:
                            minVal = collector[counter]
                    epsilon = minVal
            indexB += 1
        indexA += 1

    result: List[int] = []
    step = 0
    while step < delta:
        if step % 2 != 1:
            result.append(1)
        else:
            result.append(epsilon)
        step += 1

    return result