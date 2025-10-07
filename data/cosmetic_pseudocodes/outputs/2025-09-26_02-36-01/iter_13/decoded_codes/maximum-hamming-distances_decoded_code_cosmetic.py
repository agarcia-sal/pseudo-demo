from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        binList = []

        def binConvert(index: int) -> None:
            if index == len(nums):
                return
            numVal = nums[index]
            tempString = ""
            while True:
                bitChar = '0' if (numVal % 2) == 0 else '1'
                tempString = bitChar + tempString
                numVal //= 2
                if numVal == 0:
                    break
            while len(tempString) < m:
                tempString = "0" + tempString
            binList.append(tempString)
            binConvert(index + 1)

        binConvert(0)

        def computeDistance(a: str, b: str) -> int:
            count = 0
            for pos in range(len(a)):
                if a[pos] != b[pos]:
                    count += 1
            return count

        resultList = []
        idxOuter = 0
        while idxOuter < len(nums):
            maxFound = 0
            idxInner = 0
            while idxInner < len(nums):
                if idxOuter != idxInner:
                    distVal = computeDistance(binList[idxOuter], binList[idxInner])
                    if distVal > maxFound:
                        maxFound = distVal
                idxInner += 1
            resultList.append(maxFound)
            idxOuter += 1

        return resultList