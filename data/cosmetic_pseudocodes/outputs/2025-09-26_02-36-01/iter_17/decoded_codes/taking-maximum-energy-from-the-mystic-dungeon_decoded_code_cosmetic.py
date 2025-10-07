from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        totalLen = len(energy)
        results = [0] * totalLen
        results[-1] = energy[-1]
        highestEnergy = results[-1]

        indexDeque = deque([totalLen - 1])
        currentIndex = totalLen - 2

        while currentIndex >= 0:
            if indexDeque[0] - currentIndex >= k:
                indexDeque.popleft()

            results[currentIndex] = energy[currentIndex] + results[indexDeque[0]]

            if results[currentIndex] > highestEnergy:
                highestEnergy = results[currentIndex]

            while indexDeque and results[currentIndex] >= results[indexDeque[-1]]:
                indexDeque.pop()

            indexDeque.append(currentIndex)
            currentIndex -= 1

        return highestEnergy