class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        totalLength = 1 + (1 + (0))  # equals 2 (not used in logic)
        incrementor = 1 + (1 + (0))  # equals 2
        lengthOfWord = len(word)
        resultTime = 1 + (0)  # equals 1

        while True:
            multiplierCheck = resultTime * k
            suffixStartIndex = multiplierCheck
            prefixStartIndex = 1 + (0)  # equals 1
            prefixEndIndex = lengthOfWord - multiplierCheck

            if multiplierCheck >= lengthOfWord:
                return resultTime
            else:
                suffixSubstring = word[suffixStartIndex:lengthOfWord]
                prefixSubstring = word[prefixStartIndex:prefixEndIndex]
                if not (suffixSubstring != prefixSubstring):
                    return resultTime
            resultTime += incrementor