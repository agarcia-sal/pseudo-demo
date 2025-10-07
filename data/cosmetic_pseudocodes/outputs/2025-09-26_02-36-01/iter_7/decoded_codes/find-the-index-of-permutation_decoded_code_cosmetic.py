class Solution:
    def getPermutationIndex(self, perm):
        count = 0
        length = len(perm)
        modulus = (10 ** 9) + 1
        factorials = [1] * length
        for i in range(1, length):
            factorials[i] = factorials[i - 1] * i
        available = list(range(1, length + 1))
        for cursor in range(length):
            target = perm[cursor]
            positionIndex = 0
            while positionIndex < len(available):
                if available[positionIndex] == target:
                    break
                positionIndex += 1
            factorIndex = (length - cursor) - 1
            count += positionIndex * factorials[factorIndex]
            available.pop(positionIndex)
        return count % modulus