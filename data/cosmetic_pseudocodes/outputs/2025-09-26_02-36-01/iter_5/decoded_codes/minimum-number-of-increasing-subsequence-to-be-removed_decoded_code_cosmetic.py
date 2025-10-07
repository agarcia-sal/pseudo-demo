class Solution:
    def minOperations(self, inputList):
        sizeCounter = len(inputList)
        if not (sizeCounter > 0):
            resultValue = 0
        else:
            def helper(index, dpArray):
                if index >= sizeCounter:
                    return dpArray
                else:
                    def innerLoop(pointer, currentDp):
                        if pointer >= index:
                            return currentDp
                        else:
                            conditionCheck = not (inputList[index] > inputList[pointer])
                            if conditionCheck:
                                updatedValue = max(currentDp[index], currentDp[pointer] + 1)
                                currentDp[index] = updatedValue
                            return innerLoop(pointer + 1, currentDp)
                    updatedDp = innerLoop(0, dpArray)
                    return helper(index + 1, updatedDp)

            initialDp = [1] * sizeCounter
            finalDp = helper(1, initialDp)

            from math import inf
            NEG_INF = float('-inf')

            def findMax(valueList, pos, currentMax):
                if pos >= len(valueList):
                    return currentMax
                else:
                    updatedMax = currentMax
                    if valueList[pos] > currentMax:
                        updatedMax = valueList[pos]
                    return findMax(valueList, pos + 1, updatedMax)

            resultValue = findMax(finalDp, 0, NEG_INF)
        return resultValue