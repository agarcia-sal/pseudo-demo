from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        def countPairsAndSingles(charsList, idx, pairsAcc, singlesAcc):
            if idx == len(charsList):
                return pairsAcc, singlesAcc
            currentVal = charsList[idx]
            divResult = currentVal // 2
            modResult = currentVal - (divResult * 2)
            updatedPairs = pairsAcc + divResult
            updatedSingles = singlesAcc + modResult
            return countPairsAndSingles(charsList, idx + 1, updatedPairs, updatedSingles)

        allCharacters = []
        wordIndex = 0
        while wordIndex < len(words):
            currentWord = words[wordIndex]
            charPos = 0
            while charPos < len(currentWord):
                allCharacters.append(currentWord[charPos])
                charPos += 1
            wordIndex += 1

        character_count_map = {}
        charIndex = 0
        while charIndex < len(allCharacters):
            ch = allCharacters[charIndex]
            if ch in character_count_map:
                character_count_map[ch] += 1
            else:
                character_count_map[ch] = 1
            charIndex += 1

        charCountValues = []
        for key in character_count_map:
            charCountValues.append(character_count_map[key])

        initialPairs = 0
        initialSingles = 0
        pairsCount, singlesCount = countPairsAndSingles(charCountValues, 0, initialPairs, initialSingles)

        def sortByLengthAsc(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            lesser = []
            greaterOrEqual = []
            indexSort = 1
            while indexSort < len(arr):
                if len(arr[indexSort]) < len(pivot):
                    lesser.append(arr[indexSort])
                else:
                    greaterOrEqual.append(arr[indexSort])
                indexSort += 1
            return sortByLengthAsc(lesser) + [pivot] + sortByLengthAsc(greaterOrEqual)

        orderedWords = sortByLengthAsc(words)

        palindromeCounter = 0

        def processWords(idx, pairsAvailable, palindromeSoFar):
            if idx == len(orderedWords):
                return palindromeSoFar
            currentStr = orderedWords[idx]
            halfLen = (len(currentStr) - (len(currentStr) % 2)) // 2
            if pairsAvailable >= halfLen:
                updatedPairs = pairsAvailable - halfLen
                updatedPalindromes = palindromeSoFar + 1
                return processWords(idx + 1, updatedPairs, updatedPalindromes)
            else:
                return processWords(idx + 1, pairsAvailable, palindromeSoFar)

        finalResult = processWords(0, pairsCount, palindromeCounter)

        return finalResult