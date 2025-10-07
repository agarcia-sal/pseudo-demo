class Solution:
    def getPermutationIndex(self, perm):
        def computeFactorials(length):
            results = [1] * length
            for i in range(1, length):
                results[i] = results[i - 1] * i
            return results

        def findPosition(value, container):
            for idx, val in enumerate(container):
                if val == value:
                    return idx
            # Given the problem context, value should always be found

        size = len(perm)

        moduloValue = 10**9 + 1

        factorialList = computeFactorials(size)

        availableNumbers = list(range(1, size + 1))

        totalIndex = 0
        for stepCounter in range(size):
            currentPos = findPosition(perm[stepCounter], availableNumbers)
            totalIndex += currentPos * factorialList[(size - stepCounter) - 1]
            del availableNumbers[currentPos]

        finalResult = totalIndex % moduloValue
        return finalResult