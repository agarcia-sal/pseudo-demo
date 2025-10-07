class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        charsArray = sorted(list(s))
        totalLength = len(charsArray)
        halfIndex = totalLength // 2

        if halfIndex > 0 and charsArray[halfIndex] == charsArray[halfIndex - 1]:
            leftPointer = halfIndex
            while leftPointer < totalLength and charsArray[leftPointer] == charsArray[leftPointer - 1]:
                leftPointer += 1

            rightPointer = halfIndex
            while rightPointer < totalLength and charsArray[rightPointer] == charsArray[totalLength - rightPointer - 1]:
                if leftPointer >= totalLength:
                    return "-1"
                charsArray[leftPointer], charsArray[rightPointer] = charsArray[rightPointer], charsArray[leftPointer]
                leftPointer += 1
                rightPointer += 1

        index = 0
        while index < halfIndex:
            if charsArray[index] == charsArray[totalLength - index - 1]:
                foundSwap = False
                searchPointer = halfIndex
                while searchPointer < totalLength:
                    if charsArray[searchPointer] != charsArray[index] and charsArray[searchPointer] != charsArray[totalLength - index - 1]:
                        charsArray[searchPointer], charsArray[index] = charsArray[index], charsArray[searchPointer]
                        foundSwap = True
                        break
                    searchPointer += 1
                if not foundSwap:
                    return "-1"
            index += 1

        resultString = "".join(charsArray)
        return resultString