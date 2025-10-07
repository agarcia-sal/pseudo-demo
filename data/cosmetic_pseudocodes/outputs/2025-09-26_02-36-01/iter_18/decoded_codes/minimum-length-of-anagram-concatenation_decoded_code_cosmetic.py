class Solution:
    def minAnagramLength(self, s: str) -> int:
        delta = {}
        for i in range(len(s)):
            if s[i] not in delta:
                delta[s[i]] = 0

        omega = 0
        keys = list(delta.keys())
        idx = 0
        while idx < len(keys):
            omega += 1
            idx += 1

        return omega