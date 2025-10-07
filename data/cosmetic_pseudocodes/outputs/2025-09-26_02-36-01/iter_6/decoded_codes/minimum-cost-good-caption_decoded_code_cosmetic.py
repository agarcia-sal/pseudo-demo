class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        lenCaption = len(caption)
        if not (lenCaption >= 3):
            return ""

        charsList = list(caption)

        idxTracker = 0
        while True:
            if not (idxTracker < lenCaption):
                break

            segmentStart = idxTracker

            while True:
                if not (idxTracker < lenCaption):
                    break
                if charsList[idxTracker] != charsList[segmentStart]:
                    break
                idxTracker += 1

            segmentLength = idxTracker - segmentStart

            if segmentLength < 3:
                if segmentStart > 0 and charsList[segmentStart - 1] == charsList[segmentStart]:
                    charsList[segmentStart - 1] = charsList[segmentStart]
                    segmentStart -= 1
                    segmentLength += 1

                if idxTracker < lenCaption and charsList[idxTracker - 1] == charsList[idxTracker]:
                    charsList[idxTracker] = charsList[idxTracker - 1]
                    idxTracker += 1
                    segmentLength += 1

                if segmentLength < 3:
                    if segmentStart > 0:
                        replacementCandidate = charsList[segmentStart - 1]
                    else:
                        replacementCandidate = charsList[idxTracker]

                    if replacementCandidate == "a":
                        replacementChar = "b"
                    elif replacementCandidate == "z":
                        replacementChar = "y"
                    else:
                        replacementChar = chr(ord(replacementCandidate) + 1)

                    cursorPos = segmentStart
                    while True:
                        if not (cursorPos <= segmentStart + segmentLength - 1):
                            break
                        charsList[cursorPos] = replacementChar
                        cursorPos += 1

                    idxTracker = segmentStart + segmentLength

        return "".join(charsList)