class Solution:
    def getPermutationIndex(self, perm):
        length = len(perm)
        modulus = 10**9 + 7

        factorials = [1] * length
        for i in range(1, length):
            factorials[i] = factorials[i - 1] * i

        availableNums = list(range(1, length + 1))

        resultAcc = 0
        for idx in range(length):
            currentVal = perm[idx]
            posIndex = availableNums.index(currentVal)

            factorIdx = length - idx - 1
            incrementVal = posIndex * factorials[factorIdx]
            resultAcc += incrementVal

            del availableNums[posIndex]

        finalResult = resultAcc % modulus
        return finalResult