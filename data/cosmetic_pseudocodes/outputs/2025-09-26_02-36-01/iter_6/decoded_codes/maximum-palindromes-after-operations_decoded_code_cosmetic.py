class Solution:
    def maxPalindromesAfterOperations(self, words):
        def buildFrequencyMap(elements):
            frequencyMap = {}
            idx = 0
            while idx < len(elements):
                ch = elements[idx]
                if ch in frequencyMap:
                    frequencyMap[ch] += 1
                else:
                    frequencyMap[ch] = 1
                idx += 1
            return frequencyMap

        combinedText = ""
        pos = 0
        while True:
            if pos >= len(words):
                break
            combinedText += words[pos]
            pos += 1

        charFrequency = buildFrequencyMap(combinedText)
        totalPairs = 0
        totalSingles = 0

        def processCounts(freqValues, currentIndex, pairAcc, singleAcc):
            if currentIndex >= len(freqValues):
                return pairAcc, singleAcc
            currCount = freqValues[currentIndex]
            newPairs = pairAcc + (currCount - (currCount % 2)) // 2
            newSingles = singleAcc + (currCount % 2)
            return processCounts(freqValues, currentIndex + 1, newPairs, newSingles)

        countsArray = []
        for val in charFrequency.values():
            countsArray.append(val)

        totalPairs, totalSingles = processCounts(countsArray, 0, totalPairs, totalSingles)

        def quickLengthCompare(a, b):
            return len(a) > len(b)

        def recursiveSortDescending(arr, n):
            if n <= 1:
                return
            for i in range(n - 1):
                if not quickLengthCompare(arr[i], arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            recursiveSortDescending(arr, n - 1)

        recursiveSortDescending(words, len(words))

        palindromeCount = 0

        def attemptFormPalindrome(wordList, index, availablePairs, formedCount):
            if index >= len(wordList):
                return formedCount
            currentWord = wordList[index]
            halfSize = (len(currentWord) - (len(currentWord) % 2)) // 2
            if availablePairs >= halfSize:
                nextAvailablePairs = availablePairs - halfSize
                nextFormedCount = formedCount + 1
                return attemptFormPalindrome(wordList, index + 1, nextAvailablePairs, nextFormedCount)
            else:
                return attemptFormPalindrome(wordList, index + 1, availablePairs, formedCount)

        return attemptFormPalindrome(words, 0, totalPairs, palindromeCount)