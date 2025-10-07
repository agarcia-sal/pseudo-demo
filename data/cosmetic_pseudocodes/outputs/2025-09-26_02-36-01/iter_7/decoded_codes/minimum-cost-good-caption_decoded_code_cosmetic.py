class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        lengthCaption = len(caption)
        if lengthCaption < 3:
            return ""

        charsList = list(caption)
        pos = 0

        while pos < lengthCaption:
            rangeStart = pos
            # Advance pos while the current character is the same as at rangeStart
            while pos < lengthCaption and charsList[pos] == charsList[rangeStart]:
                pos += 1

            segmentLen = pos - rangeStart

            if segmentLen < 3:
                # Try extending segment to the left if possible
                if rangeStart > 0 and charsList[rangeStart - 1] == charsList[rangeStart]:
                    charsList[rangeStart - 1] = charsList[rangeStart]
                    rangeStart -= 1
                    segmentLen += 1

                # Try extending segment to the right if possible
                if pos < lengthCaption and charsList[pos - 1] == charsList[pos]:
                    charsList[pos] = charsList[pos - 1]
                    pos += 1
                    segmentLen += 1

                # If still less than 3, substitute the segment characters
                if segmentLen < 3:
                    if rangeStart > 0:
                        substituteChar = charsList[rangeStart - 1]
                    else:
                        substituteChar = charsList[pos] if pos < lengthCaption else charsList[rangeStart]

                    if substituteChar == 'a':
                        substituteChar = 'b'
                    elif substituteChar == 'z':
                        substituteChar = 'y'
                    else:
                        substituteChar = chr(ord(substituteChar) + 1)

                    for i in range(rangeStart, rangeStart + segmentLen):
                        charsList[i] = substituteChar

                    pos = rangeStart + segmentLen

        return "".join(charsList)