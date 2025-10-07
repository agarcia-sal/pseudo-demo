class Solution:
    def maxPalindromesAfterOperations(self, words):
        def customCounter(sequence):
            mapX = {}
            helperFillMap(sequence, mapX)
            return mapX

        def helperFillMap(seq, mapRef):
            idxA = 0
            while idxA < len(seq):
                charR = seq[idxA]
                if charR not in mapRef:
                    mapRef[charR] = 0
                mapRef[charR] += 1
                idxA += 1

        counterC = customCounter(''.join(words))

        def integerDivTwo(value):
            quotient = 0
            while (quotient + 1)*2 <= value:
                quotient += 1
            return quotient

        def moduloTwo(value):
            return value - (integerDivTwo(value) * 2)

        varM = 0
        varN = 0
        valsList = []

        def populateVals():
            for k in counterC.keys():
                valsList.append(counterC[k])

        populateVals()

        iterU = 0
        while iterU < len(valsList):
            currCount = valsList[iterU]
            varM += integerDivTwo(currCount)
            varN += moduloTwo(currCount)
            iterU += 1

        def lengthAscComparator(a, b):
            return len(a) - len(b)

        def sortByLength(arr):
            def helperSort(low, high):
                if low < high:
                    pivot = arr[high]
                    i = low - 1
                    j = low
                    while j < high:
                        if lengthAscComparator(arr[j], pivot) <= 0:
                            i += 1
                            arr[i], arr[j] = arr[j], arr[i]
                        j += 1
                    arr[i + 1], arr[high] = arr[high], arr[i + 1]
                    helperSort(low, i)
                    helperSort(i + 2, high)
            helperSort(0, len(arr) - 1)

        sortByLength(words)

        countPal = 0
        indexW = 0

        def halfLenDiv2(strn):
            return integerDivTwo(len(strn))

        while indexW < len(words):
            wStr = words[indexW]
            hLen = halfLenDiv2(wStr)
            if varM >= hLen:
                varM -= hLen
                countPal += 1
            indexW += 1

        return countPal