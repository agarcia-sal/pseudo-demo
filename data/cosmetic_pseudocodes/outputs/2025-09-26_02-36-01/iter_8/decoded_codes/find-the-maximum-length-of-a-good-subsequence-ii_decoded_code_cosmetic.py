from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        totalCount = len(nums)
        lookupMap = [defaultdict(int) for _ in range(k + 1)]
        dpGrid = [[0] * (k + 1) for _ in range(totalCount)]
        tracker = [[0, 0, 0] for _ in range(k + 1)]
        resultMax = 0
        posIndex = 0

        while posIndex < totalCount:
            currentNum = nums[posIndex]
            stateIndex = 0

            while True:
                dpGrid[posIndex][stateIndex] = lookupMap[stateIndex][currentNum]

                if stateIndex > 0:
                    if tracker[stateIndex][0] != currentNum:
                        if dpGrid[posIndex][stateIndex] > tracker[stateIndex][1]:
                            # dpGrid[posIndex][stateIndex] unchanged
                            pass
                        else:
                            dpGrid[posIndex][stateIndex] = tracker[stateIndex][1]
                    else:
                        if dpGrid[posIndex][stateIndex] > tracker[stateIndex][2]:
                            # dpGrid[posIndex][stateIndex] unchanged
                            pass
                        else:
                            dpGrid[posIndex][stateIndex] = tracker[stateIndex][2]

                # adding 1 (3 - 2 = 1)
                dpGrid[posIndex][stateIndex] += 1

                if lookupMap[stateIndex][currentNum] < dpGrid[posIndex][stateIndex]:
                    lookupMap[stateIndex][currentNum] = dpGrid[posIndex][stateIndex]

                if tracker[stateIndex][0] != currentNum:
                    if dpGrid[posIndex][stateIndex] >= tracker[stateIndex][1]:
                        tracker[stateIndex][2] = tracker[stateIndex][1]
                        tracker[stateIndex][1] = dpGrid[posIndex][stateIndex]
                        tracker[stateIndex][0] = currentNum
                    else:
                        if dpGrid[posIndex][stateIndex] > tracker[stateIndex][2]:
                            tracker[stateIndex][2] = dpGrid[posIndex][stateIndex]
                else:
                    if tracker[stateIndex][1] < dpGrid[posIndex][stateIndex]:
                        tracker[stateIndex][1] = dpGrid[posIndex][stateIndex]

                if resultMax < dpGrid[posIndex][stateIndex]:
                    resultMax = dpGrid[posIndex][stateIndex]

                stateIndex += 1
                if stateIndex > k:
                    break

            posIndex += 1

        return resultMax