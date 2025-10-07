class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        totalChars = len(caption)
        if totalChars < 3:
            return ""

        charArray = list(caption)
        pos = 0

        def nextAlphabetChar(c: str) -> str:
            if c == 'a':
                return 'b'
            elif c == 'z':
                return 'y'
            else:
                return chr(ord(c) + 1)

        while pos < totalChars:
            groupStart = pos

            while pos < totalChars and charArray[pos] == charArray[groupStart]:
                pos += 1

            groupLen = pos - groupStart

            if groupLen < 3:
                # Try extending the group to the left if possible
                if groupStart > 0 and charArray[groupStart - 1] == charArray[groupStart]:
                    charArray[groupStart - 1] = charArray[groupStart]
                    groupStart -= 1
                    groupLen += 1

                # Try extending the group to the right if possible
                if pos < totalChars and charArray[pos - 1] == charArray[pos]:
                    charArray[pos] = charArray[pos - 1]
                    pos += 1
                    groupLen += 1

                if groupLen < 3:
                    # Choose replacement character
                    if groupStart > 0:
                        chosenChar = charArray[groupStart - 1]
                    else:
                        # pos might be equal to totalChars here, ensure safe index
                        chosenChar = charArray[pos] if pos < totalChars else charArray[groupStart]

                    replacementChar = nextAlphabetChar(chosenChar)
                    for offset in range(groupLen):
                        charArray[groupStart + offset] = replacementChar
                    pos = groupStart + groupLen

        return ''.join(charArray)