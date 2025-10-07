class Solution:
    def minAnagramLength(self, s: str) -> int:
        char_map = {}
        for c in s:
            if c not in char_map:
                char_map[c] = True
        count = 0
        for key in char_map.keys():
            count += 1
        return count