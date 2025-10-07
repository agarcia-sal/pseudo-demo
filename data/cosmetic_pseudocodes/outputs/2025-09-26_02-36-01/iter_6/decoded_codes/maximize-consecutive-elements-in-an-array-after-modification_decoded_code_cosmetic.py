from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        resultCount = 0
        memoMap = {}

        def updateState(indexList: List[int], currentIndex: int):
            nonlocal resultCount
            if currentIndex >= len(indexList):
                return

            currentNum = indexList[currentIndex]
            nextKey = currentNum + 1
            prevKey = currentNum - 1

            nextVal = memoMap.get(nextKey, 0)
            calcNext = nextVal + 1

            currVal = memoMap.get(currentNum, 0)
            calcCurr = memoMap.get(prevKey, 0) + 1

            memoMap[nextKey] = calcNext
            memoMap[currentNum] = calcCurr

            tempMax1 = resultCount
            tempMax2 = memoMap[currentNum]
            tempMax3 = memoMap[nextKey]

            if not (tempMax1 >= tempMax2):
                if not (tempMax2 >= tempMax3):
                    resultCount = tempMax3
                else:
                    resultCount = tempMax2
            else:
                if not (tempMax1 >= tempMax3):
                    resultCount = tempMax3

            updateState(indexList, currentIndex + 1)

        sortedNums = sorted(nums)
        updateState(sortedNums, 0)
        return resultCount