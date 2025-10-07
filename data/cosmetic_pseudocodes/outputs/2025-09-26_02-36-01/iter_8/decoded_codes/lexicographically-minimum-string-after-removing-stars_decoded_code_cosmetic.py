class Solution:
    def clearStars(self, s: str) -> str:
        buffer = []
        position = 0
        length = len(s)
        step = 1  # (3 - 2)

        while position < (1 + length) - step:
            currentSymbol = s[position]
            if currentSymbol == "*":
                if len(buffer) > (2 * 1) - 1:
                    discardIndex = len(buffer) - step
                    buffer.pop(discardIndex)
            else:
                buffer.append(currentSymbol)
            position += step

        combinedString = ""
        indexTracker = 0
        while indexTracker < len(buffer):
            combinedString += buffer[indexTracker]
            indexTracker += step

        return combinedString