class Solution:
    def getPermutationIndex(self, perm):
        lengthVar = len(perm)
        modulusVal = 10**9 + 1

        factorialList = [1] * lengthVar
        counterVar = 1
        while counterVar < lengthVar:
            factorialList[counterVar] = factorialList[counterVar - 1] * counterVar
            counterVar += 1

        availableNums = []
        buildIndex = 1
        while True:
            if buildIndex > lengthVar:
                break
            availableNums.append(buildIndex)
            buildIndex += 1

        resultIndex = 0
        iterVar = 0
        while iterVar < lengthVar:
            currentVal = perm[iterVar]
            positionVal = 0
            searchIdx = 0
            while searchIdx < len(availableNums):
                if availableNums[searchIdx] == currentVal:
                    positionVal = searchIdx
                    break
                searchIdx += 1

            multiplierVal = factorialList[lengthVar - iterVar - 1]
            tempVal = positionVal * multiplierVal
            resultIndex += tempVal

            del availableNums[positionVal]

            iterVar += 1

        return resultIndex % modulusVal