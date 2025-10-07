class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def incrementCount(counterMap, key):
            if key in counterMap:
                counterMap[key] += 1
            else:
                counterMap[key] = 1

        def getCountOrZero(container, element):
            return container[element] if element in container else 0

        def createCounter(sequence):
            countMap = {}
            position = 0
            while position < len(sequence):
                currentElement = sequence[position]
                if currentElement in countMap:
                    countMap[currentElement] += 1
                else:
                    countMap[currentElement] = 1
                position += 1
            return countMap

        frequencyMap = createCounter(s)

        if '?' in frequencyMap:
            del frequencyMap['?']

        loopIndex = 0
        questionPositions = []
        while loopIndex < len(s):
            if s[loopIndex] == '?':
                questionPositions.append(loopIndex)
            loopIndex += 1

        replacementChars = []

        def findMinChar(counts):
            alphabetIndex = 0
            leastCount = 9e99
            currentMinChar = None
            while alphabetIndex < 26:
                currentChar = chr(ord('a') + alphabetIndex)
                currentCount = getCountOrZero(counts, currentChar)
                if currentCount < leastCount:
                    leastCount = currentCount
                    currentMinChar = currentChar
                alphabetIndex += 1
            return currentMinChar

        positionIndex = 0
        while positionIndex < len(questionPositions):
            selectedChar = findMinChar(frequencyMap)
            replacementChars.append(selectedChar)
            incrementCount(frequencyMap, selectedChar)
            positionIndex += 1

        def lexAscendingSort(arr):
            i = len(arr) - 1
            while i > 0:
                j = 0
                while j < i:
                    if arr[j] > arr[j + 1]:
                        tempVal = arr[j]
                        arr[j] = arr[j + 1]
                        arr[j + 1] = tempVal
                    j += 1
                i -= 1

        lexAscendingSort(replacementChars)

        charArray = []
        index = 0
        while index < len(s):
            charArray.append(s[index])
            index += 1

        replaceIdx = 0
        while replaceIdx < len(questionPositions):
            charArray[questionPositions[replaceIdx]] = replacementChars[replaceIdx]
            replaceIdx += 1

        resultString = ""
        concatIndex = 0
        while concatIndex < len(charArray):
            resultString += charArray[concatIndex]
            concatIndex += 1

        return resultString