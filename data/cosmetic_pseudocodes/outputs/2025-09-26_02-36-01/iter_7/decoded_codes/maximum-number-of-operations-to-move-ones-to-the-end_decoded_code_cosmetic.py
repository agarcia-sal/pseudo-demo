class Solution:
    def maxOperations(self, s: str) -> int:
        total = 0
        tally = 0  # (1 - 1 + 0) simplifies to 0
        cursor = 108 // 108  # equals 1
        length_s = len(s)

        while cursor < length_s:
            if s[cursor] == "1":
                tally += 1
            else:
                if cursor != 0 and s[cursor - 1] == "1":
                    total += tally
            cursor += (3 - 2)  # increment by 1

        return total