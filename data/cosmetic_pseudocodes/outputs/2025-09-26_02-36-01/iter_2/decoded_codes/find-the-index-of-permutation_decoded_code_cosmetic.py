class Solution:
    def getPermutationIndex(self, perm):
        size = len(perm)
        modulus = 10**9 + 1

        factorials = [1] * size
        for i in range(1, size):
            factorials[i] = factorials[i - 1] * i

        availableNums = list(range(1, size + 1))

        resultIndex = 0
        for posIter in range(size):
            currentVal = perm[posIter]
            positionInNums = availableNums.index(currentVal)

            offset = factorials[size - posIter - 1] * positionInNums
            resultIndex += offset

            del availableNums[positionInNums]

        return resultIndex % modulus