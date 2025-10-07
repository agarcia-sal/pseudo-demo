class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        charArray = sorted(s)
        lengthVal = len(charArray)
        halfLen = lengthVal // 2

        pointerOne = halfLen
        if halfLen > 0 and charArray[halfLen] == charArray[halfLen - 1]:
            while pointerOne < lengthVal and charArray[pointerOne] == charArray[pointerOne - 1]:
                pointerOne += 1

            pointerTwo = halfLen
            while pointerTwo < lengthVal and charArray[pointerTwo] == charArray[lengthVal - pointerTwo - 1]:
                if pointerOne >= lengthVal:
                    return "-1"
                # Swap charArray[pointerOne] and charArray[pointerTwo]
                charArray[pointerOne], charArray[pointerTwo] = charArray[pointerTwo], charArray[pointerOne]
                pointerOne += 1
                pointerTwo += 1

        index = 0
        while index < halfLen:
            if charArray[index] == charArray[lengthVal - index - 1]:
                foundSwap = False
                kIndex = halfLen
                while True:
                    if kIndex >= lengthVal:
                        break
                    if charArray[kIndex] != charArray[index] and charArray[kIndex] != charArray[lengthVal - index - 1]:
                        # Swap charArray[kIndex] and charArray[index]
                        charArray[kIndex], charArray[index] = charArray[index], charArray[kIndex]
                        foundSwap = True
                        break
                    kIndex += 1
                if not foundSwap:
                    return "-1"
            index += 1

        response = "".join(charArray)
        return response