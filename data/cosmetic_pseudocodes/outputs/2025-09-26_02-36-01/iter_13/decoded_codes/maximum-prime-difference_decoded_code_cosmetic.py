class Solution:
    def maximumPrimeDifference(self, nums):
        def createPrimeSet():
            primeNumbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
            primeMap = {}
            for prime in primeNumbers:
                primeMap[prime] = True
            return primeMap

        primeSet = createPrimeSet()

        def isPrimeCandidate(value):
            return value in primeSet

        firstOccurrence = -1
        lastOccurrence = -1

        def locatePrimes(startIndex, dataList):
            nonlocal firstOccurrence, lastOccurrence
            if startIndex >= len(dataList):
                return
            if isPrimeCandidate(dataList[startIndex]):
                if firstOccurrence == -1:
                    firstOccurrence = startIndex
                lastOccurrence = startIndex
            locatePrimes(startIndex + 1, dataList)

        locatePrimes(0, nums)

        return lastOccurrence - firstOccurrence