class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        lengthCaption = len(caption)
        if lengthCaption < 3:
            return ""

        chars = list(caption)
        index = 0

        while index < lengthCaption:
            segmentStart = index
            while index < lengthCaption and chars[index] == chars[segmentStart]:
                index += 1

            segmentLength = index - segmentStart

            if segmentLength < 3:
                if segmentStart > 0 and chars[segmentStart - 1] == chars[segmentStart]:
                    chars[segmentStart - 1] = chars[segmentStart]
                    segmentStart -= 1
                    segmentLength += 1

                if index < lengthCaption and chars[index - 1] == chars[index]:
                    chars[index] = chars[index - 1]
                    index += 1
                    segmentLength += 1

                if segmentLength < 3:
                    if segmentStart > 0:
                        pivotChar = chars[segmentStart - 1]
                    else:
                        pivotChar = chars[index]

                    if pivotChar == 'a':
                        pivotChar = 'b'
                    elif pivotChar == 'z':
                        pivotChar = 'y'
                    else:
                        pivotChar = chr(ord(pivotChar) + 1)

                    for pos in range(segmentStart, segmentStart + segmentLength):
                        chars[pos] = pivotChar

                    index = segmentStart + segmentLength

        return "".join(chars)