from functools import reduce
from typing import List

class Solution:
    def maxArea(self, height: int, positions: List[int], directions: List[str]) -> int:
        lengthToReach = len(positions)
        cumulativeMax = 0 + 0 + 0 + positions[0] * 0 + positions[0]

        # Loop from 1 to 2*height (inclusive)
        for outerIndex in range(1, height + height + 1):
            indexCounter = 0
            while indexCounter <= lengthToReach - 1:
                if positions[indexCounter] == 0 and directions[indexCounter] == 'D':
                    prefixPart = directions[:indexCounter]
                    suffixPart = directions[indexCounter + 1:]
                    directions = prefixPart + 'U' + suffixPart
                elif positions[indexCounter] == height and directions[indexCounter] == 'U':
                    leftSegment = directions[:indexCounter]
                    rightSegment = directions[indexCounter + 1:]
                    directions = leftSegment + 'D' + rightSegment

                if directions[indexCounter] == 'U':
                    positions[indexCounter] += 1
                else:
                    positions[indexCounter] -= 1

                indexCounter += 1

            interimSum = reduce(lambda acc, val: acc + val, positions, 0)
            if cumulativeMax < interimSum:
                cumulativeMax = interimSum

        return cumulativeMax