class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def findMinChar(freqMap, letters, idx, currentMinCount, currentMinChar):
            if idx >= len(letters):
                return currentMinChar
            letter = letters[idx]
            letterFreq = freqMap.get(letter, 0)
            if letterFreq < currentMinCount:
                return findMinChar(freqMap, letters, idx + 1, letterFreq, letter)
            else:
                return findMinChar(freqMap, letters, idx + 1, currentMinCount, currentMinChar)

        freq = {}
        for ch in s:
            if ch != '?':
                freq[ch] = freq.get(ch, 0) + 1

        questionMarkPositions = []
        positionCounter = 0
        while positionCounter < len(s):
            if s[positionCounter] == '?':
                questionMarkPositions.append(positionCounter)
            positionCounter += 1

        replacements = []
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        qIndex = 0
        while qIndex < len(questionMarkPositions):
            candidate = findMinChar(freq, alphabet, 0, len(s) + len(s), None)
            replacements.append(candidate)
            freq[candidate] = freq.get(candidate, 0) + 1
            qIndex += 1

        def insertionSort(arr):
            i = 1
            while i < len(arr):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
                i += 1
            return arr

        sortedReplacements = insertionSort(replacements)

        characters = []
        idxChar = 0
        while idxChar < len(s):
            characters.append(s[idxChar])
            idxChar += 1

        pIndex = 0
        while pIndex < len(questionMarkPositions) and pIndex < len(sortedReplacements):
            pos = questionMarkPositions[pIndex]
            repChar = sortedReplacements[pIndex]
            characters[pos] = repChar
            pIndex += 1

        resultString = ''
        k = 0
        while k < len(characters):
            resultString += characters[k]
            k += 1

        return resultString