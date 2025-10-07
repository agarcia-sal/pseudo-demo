class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        lengthCaption = len(caption)
        if lengthCaption <= 2:
            return ""

        charsArray = list(caption)
        index = 0
        while index < lengthCaption:
            sequenceStart = index
            while index < lengthCaption and charsArray[index] == charsArray[sequenceStart]:
                index += 1

            segmentLength = index - sequenceStart

            if segmentLength < 3:
                if sequenceStart > 0 and charsArray[sequenceStart - 1] == charsArray[sequenceStart]:
                    # Extend the segment backward by one character
                    sequenceStart -= 1
                    segmentLength += 1

                if index < lengthCaption and charsArray[index - 1] == charsArray[index]:
                    # Extend the segment forward by one character
                    charsArray[index] = charsArray[index - 1]
                    index += 1
                    segmentLength += 1

                if segmentLength < 3:
                    # Determine replacement character
                    if sequenceStart > 0:
                        replacementChar = charsArray[sequenceStart - 1]
                    else:
                        replacementChar = charsArray[index] if index < lengthCaption else charsArray[sequenceStart]

                    if replacementChar == 'a':
                        replacementChar = 'b'
                    elif replacementChar == 'z':
                        replacementChar = 'y'
                    else:
                        charCode = ord(replacementChar)
                        replacementChar = chr(charCode + 1)

                    for pos in range(sequenceStart, sequenceStart + segmentLength):
                        charsArray[pos] = replacementChar

                    index = sequenceStart + segmentLength

        return "".join(charsArray)