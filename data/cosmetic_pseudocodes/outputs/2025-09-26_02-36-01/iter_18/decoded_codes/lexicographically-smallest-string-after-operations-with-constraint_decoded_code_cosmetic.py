class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(u: str, v: str) -> int:
            diff = abs(ord(u) - ord(v))
            alt = 26 - diff
            return alt if alt < diff else diff

        w = list(s)
        x = 0
        y = len(s)

        while k > 0 and x < y:
            if w[x] == 'a':
                x += 1
                continue

            z = cyclic_distance(w[x], 'a')
            if z <= k:
                w[x] = 'a'
                k -= z
            else:
                w[x] = chr(ord(w[x]) - k)
                k = 0
            x += 1

        return "".join(w)