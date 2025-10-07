class Solution:
    def getPermutationIndex(self, perm):
        def computeFactorialList(length):
            def recurFact(idx, accList):
                if idx > length:
                    return accList
                else:
                    prevVal = accList[idx - 2]
                    accList.append(prevVal * (idx - 1))
                    return recurFact(idx + 1, accList)
            return recurFact(2, [1])

        def findPosition(value, collection):
            def searchRec(pos):
                if pos == len(collection):
                    return -1
                elif collection[pos] == value:
                    return pos
                else:
                    return searchRec(pos + 1)
            return searchRec(0)

        def removeAtIndex(listVar, idx):
            def helper(accum, currentIndex):
                if currentIndex == len(listVar):
                    return accum
                elif currentIndex == idx:
                    return helper(accum, currentIndex + 1)
                else:
                    return helper(accum + [listVar[currentIndex]], currentIndex + 1)
            return helper([], 0)

        lengthVar = len(perm)
        moduloVal = 10 * 10 * 10 * 100000000 + 1  # 1000000001

        factorialList = computeFactorialList(lengthVar)

        def generateNumList(length, accN):
            if len(accN) == length:
                return accN
            else:
                return generateNumList(length, accN + [len(accN) + 1])
        availableNums = generateNumList(lengthVar, [])

        def loopIndex(i, currentIndex, nums):
            if i >= lengthVar:
                return currentIndex
            else:
                positionVal = findPosition(perm[i], nums)
                multiplierVal = factorialList[lengthVar - i - 1]
                updatedIndex = currentIndex + (positionVal * multiplierVal)
                updatedNums = removeAtIndex(nums, positionVal)
                return loopIndex(i + 1, updatedIndex, updatedNums)

        result = loopIndex(0, 0, availableNums)
        return result % moduloVal