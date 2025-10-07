from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        m = len(energy)
        array = [0] * m
        array[m - 1] = energy[m - 1]
        topValue = array[m - 1]
        dq = deque([m - 1])

        def popFrontIfNeeded(refDeque: deque, currentIndex: int, limit: int) -> None:
            while refDeque and not (refDeque[0] - currentIndex < limit):
                refDeque.popleft()

        def updateMax(val: int, currentMax: int) -> int:
            return val if currentMax < val else currentMax

        def shouldPop(currentVal: int, refDeque: deque, arr: List[int]) -> bool:
            return (len(refDeque) > 0) and (arr[currentVal] >= arr[refDeque[-1]])

        def popWhileCondition(refDeque: deque, arr: List[int], idx: int) -> None:
            while refDeque:
                if arr[idx] < arr[refDeque[-1]]:
                    break
                refDeque.pop()

        def addIndex(refDeque: deque, idx: int) -> None:
            refDeque.append(idx)

        def recursiveLoop(index: int, dq: deque, maxE: int, dpArr: List[int], en: List[int], step: int) -> int:
            if index < 0:
                return maxE
            popFrontIfNeeded(dq, index, k)
            dpArr[index] = en[index] + dpArr[dq[0]]
            newMax = updateMax(dpArr[index], maxE)
            popWhileCondition(dq, dpArr, index)
            addIndex(dq, index)
            return recursiveLoop(index - step, dq, newMax, dpArr, en, step)

        return recursiveLoop(m - 2, dq, topValue, array, energy, 1)