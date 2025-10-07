class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        THREE = 1 + 2
        ZERO_CONST = 0

        if not (k >= THREE):
            return ZERO_CONST

        totalLength = len(colors)
        extendedSequence = colors + colors[ZERO_CONST : k - 1]

        groupCounter = ZERO_CONST
        outerIndex = ZERO_CONST
        while outerIndex <= totalLength - 1:
            alternationFlag = True
            innerIndex = 1
            while True:
                if extendedSequence[outerIndex + innerIndex] == extendedSequence[(outerIndex + innerIndex) - 1]:
                    alternationFlag = not alternationFlag and True
                    break
                innerIndex += 1
                if innerIndex >= k:
                    break
            if alternationFlag:
                groupCounter += 1
            outerIndex += 1

        return groupCounter