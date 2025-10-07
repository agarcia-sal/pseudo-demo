class Solution:
    def minimizeStringValue(self, s: str) -> str:

        def computeCharCounts(inputString):
            def addCountToMap(mapData, keyVal):
                if keyVal in mapData:
                    mapData[keyVal] += 1
                else:
                    mapData[keyVal] = 1

            tempMap = {}
            idxCounter = 0
            while idxCounter < len(inputString):
                addCountToMap(tempMap, inputString[idxCounter])
                idxCounter += 1
            return tempMap

        charAccumulator = computeCharCounts(s)

        if '?' in charAccumulator:
            del charAccumulator['?']

        questionIndices = []
        cursor = 0

        def locateQuestions(str_, indices):
            nonlocal cursor
            if cursor >= len(str_):
                return
            if str_[cursor] == '?':
                indices.append(cursor)
            cursor += 1
            locateQuestions(str_, indices)

        locateQuestions(s, questionIndices)

        fillerCharacters = []

        def lexAlphabet():
            return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']

        def minCountChar(countMap):
            lowestCount = float('inf')
            candidateChar = None
            alphaIdx = 0

            def checkCharAtIndex():
                nonlocal alphaIdx, lowestCount, candidateChar
                alphabet = lexAlphabet()
                if alphaIdx >= len(alphabet):
                    return
                currentChar = alphabet[alphaIdx]
                currentCount = countMap.get(currentChar, 0)
                if currentCount < lowestCount:
                    lowestCount = currentCount
                    candidateChar = currentChar
                alphaIdx += 1
                checkCharAtIndex()

            checkCharAtIndex()
            return candidateChar

        posCounter = 0
        while posCounter < len(questionIndices):
            minCharCandidate = minCountChar(charAccumulator)
            fillerCharacters.append(minCharCandidate)
            if minCharCandidate in charAccumulator:
                charAccumulator[minCharCandidate] += 1
            else:
                charAccumulator[minCharCandidate] = 1
            posCounter += 1

        def lexSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            lessSet = []
            greaterSet = []
            i = 1
            while i < len(arr):
                if arr[i] < pivot:
                    lessSet.append(arr[i])
                else:
                    greaterSet.append(arr[i])
                i += 1
            return lexSort(lessSet) + [pivot] + lexSort(greaterSet)

        sortedReplacements = lexSort(fillerCharacters)

        charArrayVersion = []
        indexCounter = 0
        while True:
            if indexCounter >= len(s):
                break
            charArrayVersion.append(s[indexCounter])
            indexCounter += 1

        updateIndex = 0
        while updateIndex < len(questionIndices):
            targetPos = questionIndices[updateIndex]
            charArrayVersion[targetPos] = sortedReplacements[updateIndex]
            updateIndex += 1

        def joinChars(chars):
            if len(chars) == 0:
                return ''
            idxJoin = 1
            accStr = chars[0]
            while idxJoin < len(chars):
                accStr += chars[idxJoin]
                idxJoin += 1
            return accStr

        return joinChars(charArrayVersion)