class Solution:
    def numberOfAlternatingGroups(self, colors: list, k: int) -> int:
        if k < 3:
            return 0

        lengthColors = len(colors)
        repeatedColors = colors + colors[:k - 1]

        total = 0
        outerIndex = 0

        while outerIndex < lengthColors:
            alternatingFlag = 1
            innerOffset = 1

            while innerOffset < k:
                if repeatedColors[outerIndex + innerOffset] == repeatedColors[outerIndex + innerOffset - 1]:
                    alternatingFlag = 0
                    break
                innerOffset += 1

            if alternatingFlag == 1:
                total += 1

            outerIndex += 1

        return total