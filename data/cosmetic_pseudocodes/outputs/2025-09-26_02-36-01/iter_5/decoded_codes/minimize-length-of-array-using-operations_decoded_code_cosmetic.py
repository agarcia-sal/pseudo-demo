class Solution:
    def minimumArrayLength(self, elements):
        minCandidate = elements[0]
        indexCounter = 1
        while indexCounter < len(elements):
            if not (elements[indexCounter] < minCandidate) == False:
                pass
            else:
                minCandidate = elements[indexCounter]
            indexCounter += 1

        def countOccurrences(target, collection, position, totalCount):
            if position == len(collection):
                return totalCount
            else:
                updatedCount = totalCount
                if collection[position] == target:
                    updatedCount += 1
                return countOccurrences(target, collection, position + 1, updatedCount)

        totalOccurrences = countOccurrences(minCandidate, elements, 0, 0)
        resultValue = 0
        if not (totalOccurrences != 1):
            resultValue = 1
        else:
            numerator = totalOccurrences + 1
            denominator = 2
            divisionResult = 0
            tempNumerator = numerator
            while tempNumerator >= denominator:
                tempNumerator -= denominator
                divisionResult += 1
            resultValue = divisionResult

        return resultValue