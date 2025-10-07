class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        result = 0
        lengthVal = len(colors)

        if k < 3:
            return 0

        buffer = colors + colors[:k - 1]

        idxOuter = 0
        while idxOuter <= lengthVal - 1:
            flagValid = True
            idxInner = 1
            while idxInner < k:
                if buffer[idxOuter + idxInner] == buffer[idxOuter + idxInner - 1]:
                    flagValid = False
                    break
                idxInner += 1

            if flagValid:
                result += 1
            idxOuter += 1

        return result