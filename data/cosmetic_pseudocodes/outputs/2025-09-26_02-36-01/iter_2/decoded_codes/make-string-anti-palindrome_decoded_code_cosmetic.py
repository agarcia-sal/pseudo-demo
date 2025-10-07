class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        charArray = sorted(s)
        lengthVal = len(charArray)
        halfIndex = lengthVal // 2

        if halfIndex > 0 and charArray[halfIndex] == charArray[halfIndex - 1]:
            forwardIdx = halfIndex
            while forwardIdx < lengthVal and charArray[forwardIdx] == charArray[forwardIdx - 1]:
                forwardIdx += 1

            backwardIdx = halfIndex
            while backwardIdx < lengthVal and charArray[backwardIdx] == charArray[lengthVal - backwardIdx - 1]:
                if forwardIdx >= lengthVal:
                    return "-1"
                charArray[forwardIdx], charArray[backwardIdx] = charArray[backwardIdx], charArray[forwardIdx]
                forwardIdx += 1
                backwardIdx += 1

        outerIndex = 0
        while outerIndex <= halfIndex - 1:
            if charArray[outerIndex] == charArray[lengthVal - outerIndex - 1]:
                replaced = False
                innerIndex = halfIndex
                while innerIndex < lengthVal:
                    if (
                        charArray[innerIndex] != charArray[outerIndex] and
                        charArray[innerIndex] != charArray[lengthVal - outerIndex - 1]
                    ):
                        charArray[innerIndex], charArray[outerIndex] = charArray[outerIndex], charArray[innerIndex]
                        replaced = True
                        break
                    innerIndex += 1
                if not replaced:
                    return "-1"
            outerIndex += 1

        return "".join(charArray)