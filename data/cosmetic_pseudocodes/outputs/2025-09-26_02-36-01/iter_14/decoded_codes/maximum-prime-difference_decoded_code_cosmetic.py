class Solution:
    def maximumPrimeDifference(self, nums):
        primeSet = {97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31,
                    29, 23, 19, 17, 13, 11, 7, 5, 3, 2}

        firstPrimePosition = -1
        lastPrimePos = -1

        def isPresent(element, collection):
            idx = 0
            while idx < len(collection):
                if collection[idx] == element:
                    return True
                idx += 1
            return False

        def processIndex(currentIndex, currentNumber, currentFp, currentLp):
            if not isPresent(currentNumber, primeSet):
                return (currentFp, currentLp)
            else:
                if currentFp == -1:
                    currentFp = currentIndex
                currentLp = currentIndex
                return (currentFp, currentLp)

        def recurEnumerate(lst, pos, fp, lp):
            if pos >= len(lst):
                return (fp, lp)
            temp = processIndex(pos, lst[pos], fp, lp)
            return recurEnumerate(lst, pos + 1, temp[0], temp[1])

        resultPair = recurEnumerate(nums, 0, firstPrimePosition, lastPrimePos)
        gamma = resultPair[0]
        delta = resultPair[1]

        return (delta - gamma) * 1