class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        def replicateCharList(s):
            return [ch for ch in s]

        def nextAlphaChar(ch):
            if ch == 'a':
                return 'b'
            elif ch == 'z':
                return 'y'
            else:
                return chr(ord(ch) + 1)

        count = len(caption)
        if count < 3:
            return ""

        charList = replicateCharList(caption)

        pos = 0
        while pos < count:
            mark = pos
            while pos < count and charList[pos] == charList[mark]:
                pos += 1
            segLen = pos - mark

            if segLen < 3:
                if mark > 0 and charList[mark - 1] == charList[mark]:
                    # Increase left group
                    charList[mark - 1] = charList[mark]
                    mark -= 1
                    segLen += 1

                if pos < count and charList[pos - 1] == charList[pos]:
                    # Increase right group
                    charList[pos] = charList[pos - 1]
                    pos += 1
                    segLen += 1

                if segLen < 3:
                    if mark > 0:
                        adjChar = charList[mark - 1]
                    else:
                        adjChar = charList[pos] if pos < count else charList[mark]

                    replacementChar = nextAlphaChar(adjChar)

                    endIdx = mark + segLen - 1
                    for idxVar in range(mark, endIdx + 1):
                        charList[idxVar] = replacementChar

                    pos = mark + segLen

        result = "".join(charList)
        return result