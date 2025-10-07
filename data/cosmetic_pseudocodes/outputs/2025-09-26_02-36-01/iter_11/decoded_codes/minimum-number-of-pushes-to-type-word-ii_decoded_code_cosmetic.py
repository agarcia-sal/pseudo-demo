class Solution:
    def minimumPushes(self, word: str) -> int:
        def countLetters(inputStr: str) -> dict:
            resultMap = {}
            for ch in inputStr:
                if ch not in resultMap:
                    resultMap[ch] = 1
                else:
                    resultMap[ch] += 1
            return resultMap

        frequencyMap = countLetters(word)
        freqValues = [frequencyMap[key] for key in frequencyMap]

        def descendingSort(arr: list) -> None:
            n = len(arr)
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        descendingSort(freqValues)

        accumulatedPushes = 0
        multiplier = 1
        keysUsed = 0

        def processFrequencies(arr: list, index: int) -> None:
            nonlocal accumulatedPushes, multiplier, keysUsed
            if index >= len(arr):
                return
            accumulatedPushes += arr[index] * multiplier
            keysUsed += 1
            if keysUsed == 8:
                keysUsed = 0
                multiplier += 1
            processFrequencies(arr, index + 1)

        processFrequencies(freqValues, 0)
        return accumulatedPushes