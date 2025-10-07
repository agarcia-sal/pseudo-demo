class Solution:
    def maxPalindromesAfterOperations(self, words):
        # Combine all words into a single string
        combined_string = "".join(words)

        charCounter = {}
        for ch in combined_string:
            charCounter[ch] = charCounter.get(ch, 0) + 1

        pCount = 0  # count of pairs (two characters) available for palindrome construction
        sCount = 0  # count of singles available (odd chars)
        for freq in charCounter.values():
            halfPairs = (freq - (freq % 2)) // 2  # number of pairs contributed by this freq
            remainderSingle = freq % 2             # leftover single character count
            pCount += halfPairs
            sCount += remainderSingle

        # Sort words by length ascendingly using insertion sort as per pseudocode.
        sortedWords = []
        for w in words:
            insertPos = len(sortedWords)
            while insertPos > 0 and len(w) < len(sortedWords[insertPos - 1]):
                insertPos -= 1
            sortedWords.insert(insertPos, w)

        palindromeCount = 0
        for w in sortedWords:
            currentLen = len(w)
            halfLenFloor = (currentLen - (currentLen % 2)) // 2
            if halfLenFloor <= pCount:
                pCount -= halfLenFloor
                palindromeCount += 1

        return palindromeCount