class Solution:
    def minimizeStringValue(self, sourceString: str) -> str:
        def constructFrequencyMap(text, outputMap):
            idx = 0
            while idx < len(text):
                currentChar = text[idx]
                val = outputMap.get(currentChar, 0)
                outputMap[currentChar] = val + 1
                idx += 1

        def removeKeyIfPresent(mapping, key):
            if key in mapping:
                del mapping[key]

        def alphabetSequence():
            resultList = []
            startCode = ord('a')
            endCode = ord('z')
            codeVar = startCode
            while codeVar <= endCode:
                resultList.append(chr(codeVar))
                codeVar += 1
            return resultList

        def sortLexical(listToSort):
            lenList = len(listToSort)
            i = 0
            while i < lenList - 1:
                j = 0
                while j < lenList - i - 1:
                    if listToSort[j] > listToSort[j + 1]:
                        listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]
                    j += 1
                i += 1

        countMap = {}
        constructFrequencyMap(sourceString, countMap)
        removeKeyIfPresent(countMap, '?')

        questionPositions = []
        posIndex = 0
        while True:
            if posIndex >= len(sourceString):
                break
            currentLetter = sourceString[posIndex]
            if currentLetter == '?':
                questionPositions.append(posIndex)
            posIndex += 1

        replacements = []

        def getCountOrZero(m, k):
            return m.get(k, 0)

        for _ in questionPositions:
            minimumCount = 1 + (2 * 2147483647)  # Large positive constant as infinity
            characterWithMinCount = None
            letters = alphabetSequence()
            letterIterator = 0
            while letterIterator < len(letters):
                letterChar = letters[letterIterator]
                currentCount = getCountOrZero(countMap, letterChar)
                if currentCount < minimumCount:
                    minimumCount = currentCount
                    characterWithMinCount = letterChar
                letterIterator += 1

            replacements.append(characterWithMinCount)
            countMap[characterWithMinCount] = getCountOrZero(countMap, characterWithMinCount) + 1

        sortLexical(replacements)

        charArray = []
        srcIndex = 0
        while True:
            if srcIndex >= len(sourceString):
                break
            charArray.append(sourceString[srcIndex])
            srcIndex += 1

        replIndex = 0
        qPosIndex = 0
        while qPosIndex < len(questionPositions):
            charArray[questionPositions[qPosIndex]] = replacements[replIndex]
            qPosIndex += 1
            replIndex += 1

        finalResult = ""
        concatIndex = 0
        while concatIndex < len(charArray):
            finalResult += charArray[concatIndex]
            concatIndex += 1

        return finalResult