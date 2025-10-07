class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def countOccurrences(inputString: str):
            mapOccurrences = {}
            cursor = 0
            while cursor < len(inputString):
                currentChar = inputString[cursor]
                if currentChar in mapOccurrences:
                    mapOccurrences[currentChar] += 1
                else:
                    mapOccurrences[currentChar] = 1
                cursor += 1
            return mapOccurrences

        occurrenceMap = countOccurrences(s)
        if '?' in occurrenceMap:
            del occurrenceMap['?']

        placeholders = []
        indexPointer = 0
        while indexPointer < len(s):
            currentSymbol = s[indexPointer]
            if currentSymbol == '?':
                placeholders.append(indexPointer)
            indexPointer += 1

        replacements = []
        placeholderCounter = 0
        max_int = 2**31 - 1  # Use large int instead of MAX_INTEGER from pseudocode
        while placeholderCounter < len(placeholders):
            smallestFrequency = max_int
            smallestLetter = None
            characterCode = ord('a')
            while characterCode <= ord('z'):
                letter = chr(characterCode)
                frequency = occurrenceMap.get(letter, 0)
                if frequency < smallestFrequency:
                    smallestFrequency = frequency
                    smallestLetter = letter
                characterCode += 1
            replacements.append(smallestLetter)
            if smallestLetter in occurrenceMap:
                occurrenceMap[smallestLetter] += 1
            else:
                occurrenceMap[smallestLetter] = 1
            placeholderCounter += 1

        def swap(listToSort, i, j):
            tempVar = listToSort[i]
            listToSort[i] = listToSort[j]
            listToSort[j] = tempVar

        sortedFlag = False
        while not sortedFlag:
            sortedFlag = True
            idxVar = 0
            while idxVar < len(replacements) - 1:
                if replacements[idxVar] > replacements[idxVar + 1]:
                    swap(replacements, idxVar, idxVar + 1)
                    sortedFlag = False
                idxVar += 1

        resultChars = list(s)
        iterIdx = 0
        while iterIdx < len(placeholders):
            resultChars[placeholders[iterIdx]] = replacements[iterIdx]
            iterIdx += 1

        outputString = ''
        outIdx = 0
        while outIdx < len(resultChars):
            outputString += resultChars[outIdx]
            outIdx += 1

        return outputString