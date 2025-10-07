class Solution:
    def numberOfAlternatingGroups(self, colors: list, k: int) -> int:
        if k <= 2:
            return 0

        lengthColors = len(colors)
        wrappedColors = []
        idx = 0
        while idx < lengthColors:
            wrappedColors.append(colors[idx])
            idx += 1

        repeatCount = 0
        while repeatCount < k - 1:
            wrappedColors.append(colors[repeatCount])
            repeatCount += 1

        validCount = 0
        startIndex = 0
        while startIndex < lengthColors:
            alternatingFlag = True
            offset = 1
            while offset < k and alternatingFlag:
                if wrappedColors[startIndex + offset] == wrappedColors[startIndex + offset - 1]:
                    alternatingFlag = False
                offset += 1
            if alternatingFlag:
                validCount += 1
            startIndex += 1

        return validCount