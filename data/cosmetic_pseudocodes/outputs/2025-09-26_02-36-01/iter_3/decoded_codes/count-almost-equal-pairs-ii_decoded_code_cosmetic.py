from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        totalPairs = 0
        frequencyMap = defaultdict(int)
        idx = 0
        while idx < len(nums):
            originalNum = nums[idx]
            candidates = {originalNum}
            digitsList = list(str(originalNum))
            digitsCount = len(digitsList)
            outerIdx = 0
            while outerIdx <= digitsCount - 1:
                innerIdx = 0
                while innerIdx <= outerIdx - 1:
                    digitsList[innerIdx], digitsList[outerIdx] = digitsList[outerIdx], digitsList[innerIdx]
                    joinedNumStr = "".join(digitsList)
                    candidates.add(int(joinedNumStr))
                    secondOuter = innerIdx + 1
                    while secondOuter <= digitsCount - 1:
                        secondInner = innerIdx + 1
                        while secondInner <= secondOuter - 1:
                            digitsList[secondInner], digitsList[secondOuter] = digitsList[secondOuter], digitsList[secondInner]
                            tempStr = "".join(digitsList)
                            candidates.add(int(tempStr))
                            digitsList[secondInner], digitsList[secondOuter] = digitsList[secondOuter], digitsList[secondInner]
                            secondInner += 1
                        secondOuter += 1
                    digitsList[innerIdx], digitsList[outerIdx] = digitsList[outerIdx], digitsList[innerIdx]
                    innerIdx += 1
                outerIdx += 1
            sumCount = 0
            for val in candidates:
                sumCount += frequencyMap[val]
            totalPairs += sumCount
            frequencyMap[originalNum] += 1
            idx += 1
        return totalPairs