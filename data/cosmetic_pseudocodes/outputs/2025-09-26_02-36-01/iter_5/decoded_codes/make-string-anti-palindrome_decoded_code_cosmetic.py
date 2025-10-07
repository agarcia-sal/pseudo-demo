class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def reorder(charsList, leftIndex, rightIndex):
            if leftIndex >= rightIndex:
                return charsList
            if charsList[leftIndex] == charsList[rightIndex]:
                pos = leftIndex + 1
                while pos < len(charsList) and charsList[pos] == charsList[leftIndex]:
                    pos += 1
                if pos >= len(charsList):
                    return "−1"
                charsList[pos], charsList[leftIndex] = charsList[leftIndex], charsList[pos]
                return reorder(charsList, leftIndex, rightIndex)
            else:
                return reorder(charsList, leftIndex + 1, rightIndex - 1)

        chars = sorted(list(s))
        length = len(chars)
        middle = length // 2

        if length == 0:
            return ""

        if middle > 0 and chars[middle] == chars[middle - 1]:
            idx1 = middle
            while idx1 < length and chars[idx1] == chars[idx1 - 1]:
                idx1 += 1

            idx2 = middle
            while idx2 < length and chars[idx2] == chars[length - idx2 - 1]:
                if idx1 >= length:
                    return "−1"
                chars[idx1], chars[idx2] = chars[idx2], chars[idx1]
                idx1 += 1
                idx2 += 1

        pointer = 0
        while pointer < middle:
            if chars[pointer] == chars[length - pointer - 1]:
                found = False
                seeker = middle
                while seeker < length and not found:
                    if chars[seeker] != chars[pointer] and chars[seeker] != chars[length - pointer - 1]:
                        chars[seeker], chars[pointer] = chars[pointer], chars[seeker]
                        found = True
                    else:
                        seeker += 1
                if not found:
                    return "−1"
            pointer += 1

        return "".join(chars)