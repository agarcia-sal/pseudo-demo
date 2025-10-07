class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelSet = {'a', 'e', 'i', 'o', 'u'}
        oddCountSegments = 0
        vowelRunLength = 0

        index = 0
        while index < len(s):
            ch = s[index]
            if ch in vowelSet:
                vowelRunLength += 1
            index += 1

        oddSegmentFlag = False
        pointer = 0
        while pointer < len(s):
            currentChar = s[pointer]
            if currentChar in vowelSet:
                oddSegmentFlag = not oddSegmentFlag
            if not oddSegmentFlag and (vowelRunLength % 2) == 1:
                oddCountSegments += 1
                vowelRunLength = 0
            elif oddSegmentFlag:
                vowelRunLength += 1
            pointer += 1

        if oddSegmentFlag and (vowelRunLength % 2) == 1:
            oddCountSegments += 1

        result = (oddCountSegments % 2) == 1
        return result