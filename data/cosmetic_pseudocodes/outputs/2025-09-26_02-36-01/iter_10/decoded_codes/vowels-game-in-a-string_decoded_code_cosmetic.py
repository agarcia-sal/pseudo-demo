class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels_collection = {'a', 'e', 'i', 'o', 'u'}

        def countVowels(index: int, length: int, acc: int) -> int:
            if index == length:
                return acc
            if s[index] in vowels_collection:
                return countVowels(index + 1, length, acc + 1)
            return countVowels(index + 1, length, acc)

        totalVowels = countVowels(0, len(s), 0)

        inOddSegmentFlag = False
        oddSegmentAccumulator = 0
        vowelSegmentCount = 0

        def processSegment(idx: int):
            nonlocal inOddSegmentFlag, oddSegmentAccumulator, vowelSegmentCount
            if idx == len(s):
                if inOddSegmentFlag and (oddSegmentAccumulator % 2) == 1:
                    vowelSegmentCount += 1
                return

            if s[idx] in vowels_collection:
                inOddSegmentFlag = not inOddSegmentFlag

            if (not inOddSegmentFlag) and ((oddSegmentAccumulator % 2) == 1):
                vowelSegmentCount += 1
                oddSegmentAccumulator = 0
            elif inOddSegmentFlag:
                oddSegmentAccumulator += 1

            processSegment(idx + 1)

        processSegment(0)

        outcomeFlag = (vowelSegmentCount % 2) == 1
        return outcomeFlag