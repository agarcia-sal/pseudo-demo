class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        totalChars = len(caption)
        if totalChars < 3:
            return ""

        charList = list(caption)

        def incrementChar(ch: str) -> str:
            if ch == 'a':
                return 'b'
            else:
                if ch == 'z':
                    return 'y'
                else:
                    return chr(ord(ch) + 1)

        pos = 0
        while pos < totalChars:
            groupStart = pos
            while pos < totalChars and charList[pos] == charList[groupStart]:
                pos += 1

            segmentLength = pos - groupStart

            if segmentLength < 3:
                if groupStart > 0 and charList[groupStart - 1] == charList[groupStart]:
                    # Extend segment backward
                    groupStart -= 1
                    segmentLength += 1

                if pos < totalChars and charList[pos - 1] == charList[pos]:
                    # Extend segment forward
                    charList[pos] = charList[pos - 1]
                    pos += 1
                    segmentLength += 1

                if segmentLength < 3:
                    if groupStart > 0:
                        substituteChar = charList[groupStart - 1]
                    else:
                        substituteChar = charList[pos] if pos < totalChars else charList[groupStart]

                    if substituteChar == 'a':
                        substituteChar = 'b'
                    elif substituteChar == 'z':
                        substituteChar = 'y'
                    else:
                        substituteChar = incrementChar(substituteChar)

                    for index in range(groupStart, groupStart + segmentLength):
                        charList[index] = substituteChar

                    pos = groupStart + segmentLength

        return "".join(charList)