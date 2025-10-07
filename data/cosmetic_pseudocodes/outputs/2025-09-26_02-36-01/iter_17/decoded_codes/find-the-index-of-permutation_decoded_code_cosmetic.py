class Solution:
    def getPermutationIndex(self, perm):
        lengthVar = len(perm)
        modulusVal = 10**9 + 1

        factorialArray = [1] * lengthVar
        for i in range(2, lengthVar):
            factorialArray[i] = factorialArray[i - 1] * i

        availableNums = list(range(1, lengthVar + 1))

        resultIndex = 0

        def helperIter(idx):
            nonlocal resultIndex
            if idx >= lengthVar:
                return
            position = 0
            while position < len(availableNums) and availableNums[position] != perm[idx]:
                position += 1

            multiplier = factorialArray[lengthVar - idx - 1] if lengthVar - idx - 1 >= 0 else 1
            resultIndex += position * multiplier

            availableNums.pop(position)

            helperIter(idx + 1)

        helperIter(0)

        return resultIndex % modulusVal