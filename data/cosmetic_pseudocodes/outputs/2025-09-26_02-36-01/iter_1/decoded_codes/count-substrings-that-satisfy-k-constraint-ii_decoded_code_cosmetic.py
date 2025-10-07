from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        length = len(s)
        zeroPrefixCounts = [0] * (length + 1)
        onePrefixCounts = [0] * (length + 1)

        for i in range(length):
            zeroPrefixCounts[i + 1] = zeroPrefixCounts[i]
            onePrefixCounts[i + 1] = onePrefixCounts[i]
            if s[i] == '0':
                zeroPrefixCounts[i + 1] += 1
            elif s[i] == '1':
                onePrefixCounts[i + 1] += 1

        def count_valid_substrings(l: int, r: int) -> int:
            totalCount = 0
            for index in range(l, r + 1):
                low, high = index, r + 1
                while low < high:
                    middle = (low + high) // 2
                    zeroInSubstr = zeroPrefixCounts[middle + 1] - zeroPrefixCounts[index]
                    oneInSubstr = onePrefixCounts[middle + 1] - onePrefixCounts[index]
                    if zeroInSubstr <= k or oneInSubstr <= k:
                        low = middle + 1
                    else:
                        high = middle
                maxEnd = low - 1
                if maxEnd >= index:
                    totalCount += (maxEnd - index + 1)
            return totalCount

        answers = []
        for leftBound, rightBound in queries:
            answers.append(count_valid_substrings(leftBound, rightBound))

        return answers