class Solution:
    def maximumPrimeDifference(self, inputList):
        def isPrime(member):
            primeCandidates = [
                2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37, 41, 43, 47, 53, 59, 61, 67,
                71, 73, 79, 83, 89, 97
            ]
            found = False
            position = 0
            while position < len(primeCandidates) and not found:
                if primeCandidates[position] == member:
                    found = True
                position += 1
            return found

        idxFirstPrime = -1
        idxLastPrime = -1

        idxCursor = 0
        while idxCursor < len(inputList):
            currentItem = inputList[idxCursor]
            if isPrime(currentItem):
                if idxFirstPrime == -1:
                    idxFirstPrime = idxCursor
                idxLastPrime = idxCursor
            idxCursor += 1

        differenceVariable = idxLastPrime - idxFirstPrime
        return differenceVariable