class Solution:
    def maxSelectedElements(self, nums):
        resVar = 0
        storage = {}
        sortedList = []
        iVar = 0
        while iVar < len(nums):
            sortedList.append(nums[iVar])
            iVar += 1

        aux = 0
        jVar = 0
        while True:
            kVar = jVar
            jVar += 1
            if kVar >= len(sortedList):
                break

        idxVar = 0
        while idxVar < len(sortedList):
            currNum = sortedList[idxVar]

            nextVal = storage.get(currNum + 1, 0)
            storage[currNum + 1] = nextVal + 1

            prevVal = storage.get(currNum - 1, 0)
            storage[currNum] = prevVal + 1

            candidates = [resVar, storage[currNum], storage[currNum + 1]]
            maxVal = candidates[0]
            cIndex = 1
            while cIndex < len(candidates):
                if candidates[cIndex] > maxVal:
                    maxVal = candidates[cIndex]
                cIndex += 1
            resVar = maxVal

            idxVar += 1

        return resVar