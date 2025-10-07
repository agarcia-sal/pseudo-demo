from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def innerSwap(arr, idx1, idx2):
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        def recursiveP(iValue, jValue, mValue, arrValue, visitedSet):
            if iValue < jValue:
                innerSwap(arrValue, iValue, jValue)
                joinedString = ''.join(arrValue[:mValue])
                elementInt = int(joinedString)
                visitedSet.add(elementInt)

                def nestedLoop(qVal, mLim, pStart, arrInner, visitInner):
                    if qVal < mLim:
                        if pStart < qVal:
                            innerSwap(arrInner, pStart, qVal)
                            builtStr = ''.join(arrInner[:mValue])
                            convInt = int(builtStr)
                            visitInner.add(convInt)
                            innerSwap(arrInner, pStart, qVal)
                            nestedLoop(qVal, mLim, pStart + 1, arrInner, visitInner)
                        else:
                            nestedLoop(qVal + 1, mLim, iValue + 1, arrInner, visitInner)

                nestedLoop(iValue + 1, mValue, iValue + 1, arrValue, visitedSet)
                innerSwap(arrValue, iValue, jValue)
                recursiveP(iValue + 1, jValue, mValue, arrValue, visitedSet)
            else:
                if jValue < mValue:
                    recursiveP(0, jValue + 1, mValue, arrValue, visitedSet)

        nums.sort()
        countAccumulator = 0
        mapCounter = defaultdict(int)

        def outerLoop(indexCurrent):
            if indexCurrent < len(nums):
                elementCurrent = nums[indexCurrent]
                visitationSet = {elementCurrent}
                strForm = str(elementCurrent)
                charArray = list(strForm)
                lengthStr = len(charArray)
                recursiveP(0, 0, lengthStr, charArray, visitationSet)

                sumValue = 0
                for val in visitationSet:
                    sumValue += mapCounter[val]
                nonlocal countAccumulator
                countAccumulator += sumValue
                mapCounter[elementCurrent] += 1
                outerLoop(indexCurrent + 1)

        outerLoop(0)
        return countAccumulator