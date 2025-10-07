class Solution:
    def clearStars(self, s: str) -> str:
        outputChain = []
        position = 0

        def processNext():
            nonlocal position
            if position >= len(s):
                return
            currentElement = s[position]
            position += 1

            if currentElement == '*':
                if outputChain:
                    outputChain.pop()
                processNext()
            else:
                outputChain.append(currentElement)
                processNext()

        processNext()

        combinedResult = ""
        indexCounter = 0
        while indexCounter < len(outputChain):
            combinedResult += outputChain[indexCounter]
            indexCounter += 1

        return combinedResult