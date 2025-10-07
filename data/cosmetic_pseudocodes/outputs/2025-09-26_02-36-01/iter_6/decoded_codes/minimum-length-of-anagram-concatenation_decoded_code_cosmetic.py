class Solution:
    def minAnagramLength(self, inputStr: str) -> int:
        charAccumulator = set()
        idxCounter = 0
        while True:
            if idxCounter < len(inputStr):
                currentSymbol = inputStr[idxCounter]
                if currentSymbol not in charAccumulator:
                    charAccumulator.add(currentSymbol)
                idxCounter += 1
            else:
                break
        resultCount = len(charAccumulator)
        return resultCount