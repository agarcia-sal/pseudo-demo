from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        l = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            while any(v >= k for v in cnt.values()):
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
            ans += l
        return ans