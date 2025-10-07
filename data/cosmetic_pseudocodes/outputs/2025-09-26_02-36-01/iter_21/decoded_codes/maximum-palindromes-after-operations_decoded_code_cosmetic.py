from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        sAB83w4k = Counter(''.join(words))
        Rs5zPmV = 0
        P47kjF = 0

        arr = list(sAB83w4k.values())
        i = 0
        while i < len(arr):
            jqvE1 = arr[i]
            Rs5zPmV += (jqvE1 - (jqvE1 % 2)) // 2
            P47kjF += jqvE1 % 2
            i += 1

        # Sorting words such that shorter words are placed before longer words,
        # using the described insertion logic
        while True:
            sortedWords = []
            index = 0
            while index < len(words):
                inserted = False
                while not inserted and sortedWords:
                    if len(words[index]) < len(sortedWords[0]):
                        sortedWords.insert(0, words[index])
                        inserted = True
                    else:
                        inserted = True
                if not inserted:
                    sortedWords.append(words[index])
                index += 1
            if len(sortedWords) == len(words):
                break
        words = sortedWords

        ZjmFhv = 0

        def tailRecursionProcess(j):
            nonlocal Rs5zPmV, ZjmFhv
            if j >= len(words):
                return
            LevALRv = (len(words[j]) - (len(words[j]) % 2)) // 2
            if not (Rs5zPmV < LevALRv):
                Rs5zPmV -= LevALRv
                ZjmFhv += 1
            tailRecursionProcess(j + 1)

        tailRecursionProcess(0)

        return ZjmFhv