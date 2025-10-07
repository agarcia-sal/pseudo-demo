from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        result = 0
        leftPointer = 0

        for index in range(len(s)):
            currentChar = s[index]
            frequency[currentChar] += 1

            # While there exists a character with frequency >= k
            while any(freq >= k for freq in frequency.values()):
                leftChar = s[leftPointer]
                frequency[leftChar] -= 1
                if frequency[leftChar] == 0:
                    del frequency[leftChar]
                leftPointer += 1

            result += leftPointer

        return result