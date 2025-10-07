from collections import Counter

class Solution:
    MODCONST = 10**9 + 7

    def getSum(self, arr):
        def auxiliary(seq):
            lengthVar = len(seq)
            arrayOne = [0] * lengthVar
            arrayTwo = [0] * lengthVar
            dictionaryA = Counter()

            for index1 in range(1, lengthVar):
                key1 = seq[index1 - 1]
                dictionaryA[key1] += 1
                arrayOne[index1] = dictionaryA[key1]

            dictionaryA = Counter()
            for index2 in range(lengthVar - 2, -1, -1):
                key2 = seq[index2 + 1]
                dictionaryA[key2] += 1
                arrayTwo[index2] = dictionaryA[key2]

            accSum = 0
            for pos in range(lengthVar):
                val = seq[pos]
                leftCount = arrayOne[pos]
                rightCount = arrayTwo[pos]
                accSum += (leftCount + rightCount + leftCount * rightCount) * val

            return accSum % self.MODCONST

        res1 = auxiliary(arr)
        leftIndex, rightIndex = 0, len(arr) - 1
        while leftIndex < rightIndex:
            arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]
            leftIndex += 1
            rightIndex -= 1
        res2 = auxiliary(arr)

        idxSum = sum(arr)

        return (res1 + res2 + idxSum) % self.MODCONST