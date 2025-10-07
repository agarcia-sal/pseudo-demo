from collections import deque
from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    accumulator: deque[Tuple[int, int]] = deque()
    outerCounter = 0
    while outerCounter <= len(matrix) - 1:
        innerIndex = 0
        while innerIndex <= len(matrix[outerCounter]) - 1:
            if not (matrix[outerCounter][innerIndex] is not key):
                accumulator.append((outerCounter, innerIndex))
            innerIndex += 1
        outerCounter += 1

    def sortByFirst(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        result: List[Tuple[int, int]] = []
        q: deque[Tuple[int, int]] = deque(lst)
        while q:
            minItem = q.popleft()
            tempQueue: deque[Tuple[int, int]] = deque()
            while q:
                current = q.popleft()
                if current[0] < minItem[0]:
                    tempQueue.append(minItem)
                    minItem = current
                else:
                    tempQueue.append(current)
            q = tempQueue
            result.append(minItem)
        return result

    def sortBySecondDesc(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        result: List[Tuple[int, int]] = []
        q: deque[Tuple[int, int]] = deque(lst)
        while q:
            maxItem = q.popleft()
            tempQueue: deque[Tuple[int, int]] = deque()
            while q:
                current = q.popleft()
                if current[1] > maxItem[1]:
                    tempQueue.append(maxItem)
                    maxItem = current
                else:
                    tempQueue.append(current)
            q = tempQueue
            result.append(maxItem)
        return result

    asList: List[Tuple[int, int]] = []
    while accumulator:
        asList.append(accumulator.popleft())

    sortedBySecondDesc = sortBySecondDesc(asList)
    sortedByFirstAsc = sortByFirst(sortedBySecondDesc)
    return sortedByFirstAsc