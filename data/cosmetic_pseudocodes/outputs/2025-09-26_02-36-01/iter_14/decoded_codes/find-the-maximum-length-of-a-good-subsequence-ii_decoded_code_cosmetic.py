from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        totalElements = len(nums)
        dpMatrix = [[0] * (k + 1) for _ in range(totalElements)]
        frequencyMaps = [defaultdict(int) for _ in range(k + 1)]
        topStats = [[0, 0, 0] for _ in range(k + 1)]  # [element, max_val, second_max_val]
        resultMax = 0

        def updateTopStats(statIndex: int, candidateValue: int, candidateElement: int) -> None:
            currentElement = topStats[statIndex][0]
            if currentElement != candidateElement:
                if candidateValue >= topStats[statIndex][1]:
                    topStats[statIndex][2] = topStats[statIndex][1]
                    topStats[statIndex][1] = candidateValue
                    topStats[statIndex][0] = candidateElement
                else:
                    topStats[statIndex][2] = max(topStats[statIndex][2], candidateValue)
            else:
                topStats[statIndex][1] = max(topStats[statIndex][1], candidateValue)

        outerCounter = 0
        while outerCounter < totalElements:
            currentNum = nums[outerCounter]
            innerCounter = 0
            while innerCounter <= k:
                dpMatrix[outerCounter][innerCounter] = frequencyMaps[innerCounter][currentNum]

                if innerCounter > 0:
                    if topStats[innerCounter - 1][0] != currentNum:
                        dpMatrix[outerCounter][innerCounter] = max(
                            dpMatrix[outerCounter][innerCounter],
                            topStats[innerCounter - 1][1]
                        )
                    else:
                        dpMatrix[outerCounter][innerCounter] = max(
                            dpMatrix[outerCounter][innerCounter],
                            topStats[innerCounter - 1][2]
                        )

                dpMatrix[outerCounter][innerCounter] += 1
                frequencyMaps[innerCounter][currentNum] = max(
                    frequencyMaps[innerCounter][currentNum],
                    dpMatrix[outerCounter][innerCounter]
                )
                updateTopStats(innerCounter, dpMatrix[outerCounter][innerCounter], currentNum)
                resultMax = max(resultMax, dpMatrix[outerCounter][innerCounter])

                innerCounter += 1
            outerCounter += 1

        return resultMax