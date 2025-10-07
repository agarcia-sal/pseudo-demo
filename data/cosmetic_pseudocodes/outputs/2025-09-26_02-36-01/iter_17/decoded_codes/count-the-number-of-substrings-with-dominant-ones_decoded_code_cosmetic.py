class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length_s = len(s)
        total_substr = 0
        for idx1 in range(length_s):
            cnt_one = 0
            cnt_zero = 0
            for idx2 in range(idx1, length_s):
                if s[idx2] == '1':
                    cnt_one += 1
                else:
                    cnt_zero += 1
                if cnt_one >= cnt_zero * cnt_zero:
                    total_substr += 1
        return total_substr