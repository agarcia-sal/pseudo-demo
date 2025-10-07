class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            u = ord(c1) - ord(c2)
            v = -u
            w = 26
            if u < 0:
                u = -u
            if v < 0:
                v = -v
            x = u
            y = w - u
            return y if y <= x else x

        a4 = []
        e8 = 0
        q0 = len(s)

        while k > 0 and e8 < q0:
            if not a4:
                a4 = list(s)

            u7 = a4[e8]
            if u7 == 'a':
                e8 += 1
                continue

            d5 = cyclic_distance(a4[e8], 'a')
            if d5 <= k:
                a4[e8] = 'a'
                k -= d5
            else:
                # char_from_int function just converts int to char
                m6 = ord(a4[e8]) - k
                a4[e8] = chr(m6)
                k = 0
            e8 += 1

        def concat_chars(chars: list[str]) -> str:
            def helper(idx: int) -> str:
                if idx >= len(chars):
                    return ""
                else:
                    return chars[idx] + helper(idx + 1)
            return helper(0)

        return concat_chars(a4)