class Solution:
    def maxPalindromesAfterOperations(self, words):
        def helperCountChars(items):
            def helperConcatAll(lst):
                def recurseConcat(idx, acc):
                    if idx < 0:
                        return acc
                    else:
                        return recurseConcat(idx - 1, lst[idx] + acc)
                return recurseConcat(len(lst) - 1, "")

            fullString = helperConcatAll(items)
            charFreqMap = {}

            def helperUpdateFreq(idx):
                if idx >= len(fullString):
                    return
                ch = fullString[idx]
                if ch in charFreqMap:
                    charFreqMap[ch] += 1
                else:
                    charFreqMap[ch] = 1
                helperUpdateFreq(idx + 1)

            helperUpdateFreq(0)
            return charFreqMap

        frequency = helperCountChars(words)
        countPairs = 0
        countSingles = 0

        def iterateValues(lst, idx):
            nonlocal countPairs, countSingles
            if idx >= len(lst):
                return
            currVal = lst[idx]
            countPairs += currVal // 2
            countSingles += currVal % 2
            iterateValues(lst, idx + 1)

        freqValues = [frequency[key] for key in frequency.keys()]
        iterateValues(freqValues, 0)

        def cmpLenAsc(a, b):
            if len(a) < len(b):
                return -1
            elif len(a) > len(b):
                return 1
            else:
                return 0

        def recursiveInsertionSort(arr, n):
            if n <= 1:
                return
            recursiveInsertionSort(arr, n - 1)
            lastElem = arr[n - 1]
            j = n - 2
            while j >= 0 and len(arr[j]) > len(lastElem):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = lastElem

        recursiveInsertionSort(words, len(words))

        totalPalindromes = 0

        def processWord(idx):
            nonlocal countPairs, totalPalindromes
            if idx >= len(words):
                return
            currWord = words[idx]
            halfLen = len(currWord) // 2
            if countPairs >= halfLen:
                countPairs -= halfLen
                totalPalindromes += 1
            processWord(idx + 1)

        processWord(0)

        return totalPalindromes