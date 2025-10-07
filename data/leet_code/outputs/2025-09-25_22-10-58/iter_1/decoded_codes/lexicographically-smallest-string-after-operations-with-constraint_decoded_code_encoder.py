class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            diff = abs(ord(c1) - ord(c2))
            return min(diff, 26 - diff)

        t = list(s)
        i = 0
        n = len(s)

        while k > 0 and i < n:
            if t[i] == 'a':
                i += 1
                continue

            dist_to_a = cyclic_distance(t[i], 'a')

            if dist_to_a <= k:
                t[i] = 'a'
                k -= dist_to_a
            else:
                t[i] = chr(ord(t[i]) - k)
                k = 0
            i += 1

        return ''.join(t)