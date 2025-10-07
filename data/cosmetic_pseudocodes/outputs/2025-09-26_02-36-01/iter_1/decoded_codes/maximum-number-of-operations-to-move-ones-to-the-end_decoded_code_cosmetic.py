class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        cnt = 0
        for i in range(len(s)):
            c = s[i]
            if c == '1':
                cnt += 1
            elif i > 0 and s[i - 1] == '1':
                ans += cnt
        return ans