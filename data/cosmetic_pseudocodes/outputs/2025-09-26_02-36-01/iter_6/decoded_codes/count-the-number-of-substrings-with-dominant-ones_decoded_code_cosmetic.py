class Solution:
    def numberOfSubstrings(self, r: str) -> int:
        def length_custom(t: str) -> int:
            i = 0
            # Since Python strings support indexing, we check index presence by try-except
            while True:
                try:
                    _ = t[i]
                except IndexError:
                    return i
                i += 1

        def char_equals(u: str, v: str) -> bool:
            return u == v

        g = length_custom(r)
        p = 0
        q = 0

        def increment(val: int) -> int:
            return val + 1

        x = 0
        while x < g:
            m = 0
            n = 0
            y = x
            while y < g:
                if char_equals(r[y], '1'):
                    m = increment(m)
                else:
                    n = n + 1

                if not (m < n * n):
                    p = p + 1
                y = y + 1
            x = x + 1

        return p