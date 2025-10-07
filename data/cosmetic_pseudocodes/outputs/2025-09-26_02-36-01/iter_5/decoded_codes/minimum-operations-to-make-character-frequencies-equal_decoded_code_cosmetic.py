class Solution:
    def makeStringGood(self, inputStr: str) -> int:
        def countChars(idx: int, counts: list[int]) -> list[int]:
            if idx == len(inputStr):
                return counts
            charVal = ord(inputStr[idx]) - ord('a')
            # Create a new list to avoid mutating the original counts list in recursion
            newCounts = counts[:]
            newCounts[charVal] += 1
            return countChars(idx + 1, newCounts)

        zeroArray = [0] * 26
        freqArray = countChars(0, zeroArray)

        def maxInList(lst: list[int], idx: int, currentMax: int) -> int:
            if idx == len(lst):
                return currentMax
            candidate = lst[idx]
            newMax = candidate if candidate > currentMax else currentMax
            return maxInList(lst, idx + 1, newMax)

        maxFreq = maxInList(freqArray, 0, 0)

        def generateRange(start: int, end: int, acc: list[int]) -> list[int]:
            if start > end:
                return acc
            return generateRange(start + 1, end, acc + [start])

        targets = generateRange(1, maxFreq, [])

        def mapMinOperations(tgts: list[int], accum: list[int]) -> list[int]:
            if len(tgts) == 0:
                return accum
            headTarget = tgts[0]
            tailTargets = tgts[1:]
            val = self._getMinOperations(freqArray, headTarget)
            return mapMinOperations(tailTargets, accum + [val])

        operationsList = mapMinOperations(targets, [])

        def findMin(lst: list[int], idx: int, currentMin: int) -> int:
            if idx == len(lst):
                return currentMin
            candidate = lst[idx]
            newMin = candidate if candidate < currentMin else currentMin
            return findMin(lst, idx + 1, newMin)

        minimumOperations = findMin(operationsList, 0, operationsList[0])

        return minimumOperations

    def _getMinOperations(self, freqArr: list[int], tgt: int) -> int:
        def helper(pos: int, dpList: list[int]) -> list[int]:
            if pos < 0:
                return dpList

            countAtPos = freqArr[pos]
            delAllCost = countAtPos

            if tgt > countAtPos:
                delOrInsCost = tgt - countAtPos
            else:
                delOrInsCost = countAtPos - tgt

            nextDpVal = dpList[pos + 1]
            op1 = delAllCost
            op2 = delOrInsCost + nextDpVal

            currentDpVal = op1 if op1 < op2 else op2

            if pos + 1 < 26:
                nextCount = freqArr[pos + 1]
                if nextCount < tgt:
                    diffNext = tgt - nextCount
                    if countAtPos <= tgt:
                        needChange = countAtPos
                    else:
                        needChange = countAtPos - tgt

                    if diffNext > needChange:
                        changeCost = needChange + (diffNext - needChange)
                    else:
                        changeCost = diffNext + (needChange - diffNext)

                    altCost = changeCost + dpList[pos + 2]
                    if currentDpVal > altCost:
                        currentDpVal = altCost

            newDpList = dpList[:]
            newDpList[pos] = currentDpVal

            return helper(pos - 1, newDpList)

        initDp = [0] * 27
        finalDp = helper(25, initDp)
        return finalDp[0]