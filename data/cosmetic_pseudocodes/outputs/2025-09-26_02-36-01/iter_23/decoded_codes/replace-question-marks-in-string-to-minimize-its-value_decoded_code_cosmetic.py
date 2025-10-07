class Solution:
    def minimizeStringValue(self, s):
        def countOccurrences(seq):
            countsDict = {}

            def helper(idx):
                if idx >= len(seq):
                    return
                currentItem = seq[idx]
                countsDict[currentItem] = countsDict.get(currentItem, 0) + 1
                helper(idx + 1)

            helper(0)
            return countsDict

        def getKeys(dictObj):
            keyList = []

            def collectKeys(idx, keys):
                if idx >= len(keys):
                    return
                keyList.append(keys[idx])
                collectKeys(idx + 1, keys)

            collectKeys(0, list(dictObj.keys()))
            return keyList

        tempCounter = countOccurrences(s)
        if '?' in tempCounter:
            del tempCounter['?']

        positionsList = []

        def findPositions(currentIndex):
            if currentIndex >= len(s):
                return
            currentChar = s[currentIndex]
            if currentChar == '?':
                positionsList.append(currentIndex)
            findPositions(currentIndex + 1)

        findPositions(0)

        replacementsList = []

        def findMinChar():
            alphabetSequence = [chr(ord('a') + i) for i in range(26)]
            idxAlpha = 0
            minimalChar = None
            minimalCount = float('inf')
            while idxAlpha < len(alphabetSequence):
                letter = alphabetSequence[idxAlpha]
                letterCount = tempCounter.get(letter, 0)
                if letterCount < minimalCount:
                    minimalChar = letter
                    minimalCount = letterCount
                idxAlpha += 1
            return minimalChar

        def processReplacements(posIdx):
            if posIdx >= len(positionsList):
                return
            currentChar = findMinChar()
            replacementsList.append(currentChar)
            tempCounter[currentChar] = tempCounter.get(currentChar, 0) + 1
            processReplacements(posIdx + 1)

        processReplacements(0)

        def sortListAsc(lst):
            lengthLst = len(lst)

            def sortHelper(p):
                if p >= lengthLst:
                    return
                q = p + 1
                while q < lengthLst:
                    if lst[p] > lst[q]:
                        tempChar = lst[p]
                        lst[p] = lst[q]
                        lst[q] = tempChar
                    q += 1
                sortHelper(p + 1)

            sortHelper(0)

        sortListAsc(replacementsList)

        sCharList = []

        def createCharList(idx):
            if idx >= len(s):
                return
            sCharList.append(s[idx])
            createCharList(idx + 1)

        createCharList(0)

        def assignReplacements(idx):
            if idx >= len(positionsList):
                return
            sCharList[positionsList[idx]] = replacementsList[idx]
            assignReplacements(idx + 1)

        assignReplacements(0)

        def concatenateChars(lst, pos, acc):
            if pos >= len(lst):
                return acc
            return concatenateChars(lst, pos + 1, acc + lst[pos])

        return concatenateChars(sCharList, 0, "")