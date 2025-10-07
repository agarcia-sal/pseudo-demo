class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        if k < 3:
            return 0

        lengthColors = len(colors)
        duplicatedColors = colors[:] + colors[:k]

        def checkSequence(startPos):
            if k == 1:
                return True

            posCheck = 1

            def innerLoop():
                nonlocal posCheck
                if posCheck >= k:
                    return
                if duplicatedColors[startPos + posCheck] == duplicatedColors[startPos + posCheck - 1]:
                    return False
                else:
                    posCheck += 1
                    return innerLoop()

            result = innerLoop()
            if result is False:
                return False
            else:
                return True

        validCount = 0
        currentPos = 0
        while currentPos < lengthColors:
            if checkSequence(currentPos):
                validCount += 1
            currentPos += 1

        return validCount