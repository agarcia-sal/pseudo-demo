class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        totalChars = len(caption)

        if totalChars < 3:
            return ""

        charList = list(caption)
        posCounter = 0

        while posCounter < totalChars:
            blockStart = posCounter

            while posCounter < totalChars and charList[posCounter] == charList[blockStart]:
                posCounter += 1

            groupLen = posCounter - blockStart

            if groupLen < 3:
                if blockStart > 0 and charList[blockStart - 1] == charList[blockStart]:
                    charList[blockStart - 1] = charList[blockStart]
                    blockStart -= 1
                    groupLen += 1

                if posCounter < totalChars and charList[posCounter - 1] == charList[posCounter]:
                    charList[posCounter] = charList[posCounter - 1]
                    posCounter += 1
                    groupLen += 1

                if groupLen < 3:
                    if blockStart > 0:
                        replacementChar = charList[blockStart - 1]
                    else:
                        replacementChar = charList[posCounter]

                    if replacementChar == "a":
                        replacementChar = "b"
                    elif replacementChar == "z":
                        replacementChar = "y"
                    else:
                        replacementChar = chr(ord(replacementChar) + 1)

                    for iteratorVal in range(blockStart, blockStart + groupLen):
                        charList[iteratorVal] = replacementChar

                    posCounter = blockStart + groupLen

        resultStr = ""
        concatIndex = 0

        while True:
            if concatIndex >= totalChars:
                break
            resultStr += charList[concatIndex]
            concatIndex += 1

        return resultStr