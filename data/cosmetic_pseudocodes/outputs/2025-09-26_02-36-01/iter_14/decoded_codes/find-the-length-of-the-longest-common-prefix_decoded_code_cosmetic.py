class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        def convertToStr(value: int) -> str:
            return str(value)

        SetA = set()
        for val in arr1:
            tempStr = convertToStr(val)
            for pos in range(1, len(tempStr) + 1):
                SetA.add(tempStr[:pos])

        SetB = set()
        pointer = 0
        while pointer < len(arr2):
            currentVal = arr2[pointer]
            strVal = convertToStr(currentVal)
            for counter in range(1, len(strVal) + 1):
                SetB.add(strVal[:counter])
            pointer += 1

        maxLen = 0
        for maybePrefix in SetA:
            if maybePrefix in SetB and len(maybePrefix) > maxLen:
                maxLen = len(maybePrefix)

        return maxLen