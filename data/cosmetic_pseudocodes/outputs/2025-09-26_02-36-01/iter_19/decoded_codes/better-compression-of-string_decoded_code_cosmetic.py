from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        def toDigit(c: str) -> int:
            return ord(c) - ord("0")

        accumulator = defaultdict(int)
        tempHolder = ""
        countHolder = 0
        idx = 0

        while idx < len(compressed):
            currentSymbol = compressed[idx]
            if ("A" <= currentSymbol <= "Z") or ("a" <= currentSymbol <= "z"):
                if tempHolder != "":
                    accumulator[tempHolder] += countHolder
                tempHolder = currentSymbol
                countHolder = 0
            else:
                countHolder = countHolder * 10 + toDigit(currentSymbol)
            idx += 1

        if tempHolder != "":
            accumulator[tempHolder] += countHolder

        sortedKeys = sorted(accumulator.keys())

        def buildSegment(keyChar: str) -> str:
            return keyChar + str(accumulator[keyChar])

        resultSegments = []
        position = 0
        while position < len(sortedKeys):
            resultSegments.append(buildSegment(sortedKeys[position]))
            position += 1

        finalResult = "".join(resultSegments)
        return finalResult