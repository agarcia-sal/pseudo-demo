from typing import List


class Solution:
    def maxPathLength(self, coordinates: List[List[int]], p: int) -> int:
        def _appendLeft(coords: List[List[int]], boundX: int, boundY: int) -> List[List[int]]:
            acc = []
            idx = 0
            while idx < len(coords):
                a, b = coords[idx]
                if a < boundX and b < boundY:
                    acc.append([a, b])
                idx += 1
            return acc

        def _appendRight(coords: List[List[int]], boundX: int, boundY: int) -> List[List[int]]:
            outList = []
            cursor = 0
            length = len(coords)
            while cursor < length:
                c, d = coords[cursor]
                if not (c <= boundX or d <= boundY):
                    outList.append([c, d])
                cursor += 1
            return outList

        refX, refY = coordinates[p]
        leftSet = _appendLeft(coordinates, refX, refY)
        rightSet = _appendRight(coordinates, refX, refY)

        return 1 + self._lengthOfLIS(leftSet) + self._lengthOfLIS(rightSet)

    def _lengthOfLIS(self, coordsList: List[List[int]]) -> int:
        def _bisectLeft(arr: List[int], val: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < val:
                    low = mid + 1
                else:
                    high = mid
            return low

        sortedList = coordsList[:]

        m = len(sortedList)
        if m > 1:
            for j in range(m - 1):
                for l in range(j + 1, m):
                    cond1 = sortedList[j][0] > sortedList[l][0]
                    cond2 = (sortedList[j][0] == sortedList[l][0]) and (sortedList[j][1] < sortedList[l][1])
                    if cond1 or cond2:
                        sortedList[j], sortedList[l] = sortedList[l], sortedList[j]

        pile = []
        index = 0
        while index < len(sortedList):
            valY = sortedList[index][1]
            if not pile:
                pile.append(valY)
            else:
                last = pile[-1]
                if valY > last:
                    pile.append(valY)
                else:
                    pos = _bisectLeft(pile, valY)
                    pile[pos] = valY
            index += 1

        return len(pile)