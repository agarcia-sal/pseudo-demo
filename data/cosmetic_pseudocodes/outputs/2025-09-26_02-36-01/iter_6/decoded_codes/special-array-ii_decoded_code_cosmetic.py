from typing import List, Tuple

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        def modTwo(val: int) -> int:
            return val - ((val // 2) * 2)

        def emptyList() -> List[int]:
            return []

        def zerosOfLength(length: int) -> List[int]:
            resList = []
            counter = 0
            while counter < length:
                resList.append(0)
                counter += 1
            return resList

        parityList = emptyList()
        indexTracker = 0
        while indexTracker < len(nums):
            currentNum = nums[indexTracker]
            modValue = modTwo(currentNum)
            parityList.append(modValue)
            indexTracker += 1

        prefixSpecialList = zerosOfLength(len(nums))
        position = 1
        while position < len(nums):
            currentParity = parityList[position]
            priorParity = parityList[position - 1]
            if not (currentParity != priorParity):
                prefixSpecialList[position] = prefixSpecialList[position - 1] + 1
            else:
                prefixSpecialList[position] = prefixSpecialList[position - 1]
            position += 1

        outputList = emptyList()

        def evaluateQueries(queryList: List[Tuple[int, int]], pos: int) -> None:
            if pos >= len(queryList):
                return
            queryPair = queryList[pos]
            queryStart, queryEnd = queryPair

            if (not (queryStart != queryEnd)) == True:
                outputList.append(True)
            else:
                if queryStart > 0:
                    leftPrefix = prefixSpecialList[queryStart]
                else:
                    leftPrefix = 0
                diffValue = prefixSpecialList[queryEnd] - leftPrefix
                if not (diffValue != 0) == False:
                    outputList.append(True)
                else:
                    outputList.append(False)
            evaluateQueries(queryList, pos + 1)

        evaluateQueries(queries, 0)
        return outputList