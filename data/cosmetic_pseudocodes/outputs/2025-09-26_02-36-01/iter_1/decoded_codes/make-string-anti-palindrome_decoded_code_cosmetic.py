class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        chars = list(s)
        chars.sort()
        length = len(chars)
        half = length // 2

        if half > 0 and chars[half] == chars[half - 1]:
            leftIndex = half
            while leftIndex < length and chars[leftIndex] == chars[leftIndex - 1]:
                leftIndex += 1

            rightIndex = half
            while rightIndex < length and chars[rightIndex] == chars[length - rightIndex - 1]:
                if leftIndex >= length:
                    return "-1"
                chars[leftIndex], chars[rightIndex] = chars[rightIndex], chars[leftIndex]
                leftIndex += 1
                rightIndex += 1

        for frontIndex in range(half):
            if chars[frontIndex] == chars[length - frontIndex - 1]:
                foundSwap = False
                for backIndex in range(half, length):
                    if chars[backIndex] != chars[frontIndex] and chars[backIndex] != chars[length - frontIndex - 1]:
                        chars[backIndex], chars[frontIndex] = chars[frontIndex], chars[backIndex]
                        foundSwap = True
                        break
                if not foundSwap:
                    return "-1"

        return "".join(chars)