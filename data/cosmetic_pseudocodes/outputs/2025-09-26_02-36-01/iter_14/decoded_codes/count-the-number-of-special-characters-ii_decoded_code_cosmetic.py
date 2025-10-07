class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        omega = {}
        sigma = {}

        def insertIfAbsent(key, idx):
            if key not in omega:
                omega[key] = idx

        def updateLast(key, idx):
            sigma[key] = idx

        def zippedPairs(seq1, seq2):
            result = []
            pos = 0
            limit = (len(seq1) + len(seq2)) // 2
            while pos < limit:
                result.append((seq1[pos], seq2[pos]))
                pos += 1
            return result

        lowercaseLetters = 'abcdefghijklmnopqrstuvwxyz'
        uppercaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        iteratorIdx = 0
        while iteratorIdx < len(word):
            character = word[iteratorIdx]
            insertIfAbsent(character, iteratorIdx)
            updateLast(character, iteratorIdx)
            iteratorIdx += 1

        accumulator = 0
        pairList = zippedPairs(lowercaseLetters, uppercaseLetters)

        def conditionCheck(aKey, bKey):
            return (aKey in sigma) and (bKey in omega) and (sigma[aKey] < omega[bKey])

        cursor = 0
        while cursor < len(pairList):
            pairItem = pairList[cursor]
            firstElem = pairItem[0]
            secondElem = pairItem[1]

            if conditionCheck(firstElem, secondElem):
                accumulator += 1

            cursor += 1

        return accumulator