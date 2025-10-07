from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        def customCounter(sequence):
            freqMap = {}
            for ch in sequence:
                if ch not in freqMap:
                    freqMap[ch] = 0
                freqMap[ch] += 1
            return freqMap

        acc_characters = []
        for idx in range(len(words)):
            for character in words[idx]:
                acc_characters.append(character)

        histogram = customCounter(acc_characters)

        total_pairs = 0
        leftover_singles = 0

        countsList = list(histogram.values())
        position = 0
        while position < len(countsList):
            current_count = countsList[position]
            total_pairs += current_count // 2
            leftover_singles += current_count % 2
            position += 1

        def measureLength(item):
            return len(item)

        def ascendingOrder(arr):
            n = len(arr)
            while True:
                swapped = False
                i = 0
                while i < n - 1:
                    if measureLength(arr[i]) > measureLength(arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swapped = True
                    i += 1
                n -= 1
                if not swapped:
                    break
            return arr

        sortedWords = ascendingOrder(words)

        palindrome_count = 0
        indexVar = 0

        while True:
            if indexVar >= len(sortedWords):
                break
            currentWord = sortedWords[indexVar]
            segment = len(currentWord) // 2
            if total_pairs >= segment:
                total_pairs -= segment
                palindrome_count += 1
            indexVar += 1

        return palindrome_count