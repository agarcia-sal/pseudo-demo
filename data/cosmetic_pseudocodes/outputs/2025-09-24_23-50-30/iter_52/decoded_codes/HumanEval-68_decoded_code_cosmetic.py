from typing import List, Tuple

def pluck(collection: List[int]) -> List[int]:
    if len(collection) == 0:
        return []

    def findEvens(source: List[int], acc: List[int], idx: int) -> List[int]:
        if idx == len(source):
            return acc
        # Check if source[idx] is even
        if source[idx] % 2 == 0:
            newAcc = acc + [source[idx]]
        else:
            newAcc = acc
        return findEvens(source, newAcc, idx + 1)

    gatheredEvens = findEvens(collection, [], 0)

    if len(gatheredEvens) == 0:
        return []

    def locateMinimum(
        items: List[int], currentMin: int, currentIdx: int, minIdx: int, pos: int
    ) -> Tuple[int, int]:
        if pos == len(items):
            return (currentMin, minIdx)
        elif items[pos] < currentMin:
            return locateMinimum(items, items[pos], pos, pos, pos + 1)
        else:
            return locateMinimum(items, currentMin, currentIdx, minIdx, pos + 1)

    minEntry = locateMinimum(gatheredEvens, gatheredEvens[0], 0, 0, 1)
    minimumItem, minimumPosition = minEntry

    def findIndex(target: int, array: List[int], position: int) -> int:
        if position == len(array):
            return -1
        elif array[position] == target:
            return position
        else:
            return findIndex(target, array, position + 1)

    originalIndex = findIndex(minimumItem, collection, 0)

    return [minimumItem, originalIndex]