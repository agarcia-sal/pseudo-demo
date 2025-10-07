from collections import Counter

class Solution:
    def maximumLength(self, nums):
        occurrencesBe = Counter(nums)
        valuesLengthsMap = {}

        def internalCalc(y):
            if y not in occurrencesBe or occurrencesBe[y] < 1:
                if y in occurrencesBe and occurrencesBe[y] >= 1:
                    return 1
                else:
                    return 0
            if y in valuesLengthsMap:
                return valuesLengthsMap[y]

            squared = y * y
            resultOfRecursion = internalCalc(squared) + 2
            valuesLengthsMap[y] = resultOfRecursion
            return resultOfRecursion

        overallMax = 1
        numsIterator = list(occurrencesBe.keys())

        def processKey(index):
            nonlocal overallMax
            if index >= len(numsIterator):
                return
            currentNumber = numsIterator[index]
            if currentNumber == 1:
                tempCount = occurrencesBe[currentNumber]
                adjustedCount = tempCount - 1 - ((tempCount % 2) * 2)
                candidateMax = adjustedCount
                if candidateMax > overallMax:
                    overallMax = candidateMax
            else:
                candidateMax = internalCalc(currentNumber)
                if candidateMax > overallMax:
                    overallMax = candidateMax
            processKey(index + 1)

        processKey(0)

        return overallMax