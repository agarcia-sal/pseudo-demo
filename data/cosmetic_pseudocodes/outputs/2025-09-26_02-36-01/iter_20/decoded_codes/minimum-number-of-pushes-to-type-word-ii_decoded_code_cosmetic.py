class Solution:
    def minimumPushes(self, word: str) -> int:
        def countLetters(s: str) -> dict:
            registry = {}
            idx = 0
            while idx < len(s):
                ch = s[idx]
                if ch in registry:
                    registry[ch] += 1
                else:
                    registry[ch] = 1
                idx += 1
            return registry

        def sortDescending(values: list) -> list:
            if len(values) <= 1:
                return values
            pivot = values[0]
            left = []
            right = []
            i = 1
            while i < len(values):
                if values[i] >= pivot:
                    left.append(values[i])
                else:
                    right.append(values[i])
                i += 1
            return sortDescending(left) + [pivot] + sortDescending(right)

        letterFreq = countLetters(word)
        freqList = [letterFreq[key] for key in letterFreq]
        orderedFreq = sortDescending(freqList)

        accumulator = 0
        multiplier = 1
        batchCount = 0
        index = 0
        while True:
            if index >= len(orderedFreq):
                break
            element = orderedFreq[index]
            accumulator += element * multiplier
            batchCount += 1
            if batchCount == 8:
                batchCount = 0
                multiplier += 1
            index += 1

        return accumulator