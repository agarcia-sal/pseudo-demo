class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        lengthCaption = len(caption)
        if lengthCaption < 3:
            return ""

        charsList = list(caption)
        pos = 0

        while pos < lengthCaption:
            segmentStart = pos

            while pos < lengthCaption and charsList[pos] == charsList[segmentStart]:
                pos += 1
            segmentLength = pos - segmentStart

            if segmentLength < 3:
                if segmentStart > 0 and charsList[segmentStart - 1] == charsList[segmentStart]:
                    charsList[segmentStart - 1] = charsList[segmentStart]
                    segmentStart -= 1
                    segmentLength += 1

                if pos < lengthCaption and charsList[pos - 1] == charsList[pos]:
                    charsList[pos] = charsList[pos - 1]
                    pos += 1
                    segmentLength += 1

                if segmentLength < 3:
                    if segmentStart > 0:
                        replacementChar = charsList[segmentStart - 1]
                    else:
                        replacementChar = charsList[pos] if pos < lengthCaption else charsList[segmentStart]

                    if replacementChar == 'a':
                        replacementChar = 'b'
                    elif replacementChar == 'z':
                        replacementChar = 'y'
                    else:
                        replacementChar = chr(ord(replacementChar) + 1)

                    for index in range(segmentStart, segmentStart + segmentLength):
                        charsList[index] = replacementChar

                    pos = segmentStart + segmentLength

        return "".join(charsList)