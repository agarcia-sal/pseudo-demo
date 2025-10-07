class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def computeFrequencies(inputWord):
            freqDict = {}
            def loopChars(position):
                if position >= len(inputWord):
                    return freqDict
                currentChar = inputWord[position]
                if currentChar in freqDict:
                    freqDict[currentChar] += 1
                else:
                    freqDict[currentChar] = 1
                return loopChars(position + 1)
            return loopChars(0)

        freqMap = computeFrequencies(word)
        freqList = [freqMap[key] for key in freqMap]

        def ascendingSort(listToSort):
            if len(listToSort) <= 1:
                return listToSort
            pivot = listToSort[0]
            lessPart, equalPart, greaterPart = [], [], []

            def partition(index):
                if index >= len(listToSort):
                    return
                element = listToSort[index]
                if element < pivot:
                    lessPart.append(element)
                elif element == pivot:
                    equalPart.append(element)
                else:
                    greaterPart.append(element)
                partition(index + 1)

            partition(0)
            return ascendingSort(lessPart) + equalPart + ascendingSort(greaterPart)

        sortedFreqList = ascendingSort(freqList)

        infiniteVal = float('inf')
        minimumDeletion = infiniteVal

        def loopIndex(i):
            nonlocal minimumDeletion
            if i >= len(sortedFreqList):
                return
            maxAllowedFrequency = sortedFreqList[i] + k
            deletionSum = 0

            def processRight(j):
                nonlocal deletionSum
                if j >= len(sortedFreqList):
                    return
                if sortedFreqList[j] > maxAllowedFrequency:
                    diff = sortedFreqList[j] - maxAllowedFrequency
                    deletionSum += diff
                processRight(j + 1)

            processRight(i + 1)

            def processLeft(j):
                nonlocal deletionSum
                if j < 0:
                    return
                deletionSum += sortedFreqList[j]
                processLeft(j - 1)

            processLeft(i - 1)

            if deletionSum < minimumDeletion:
                minimumDeletion = deletionSum

            loopIndex(i + 1)

        loopIndex(0)
        return minimumDeletion