class Solution:
    def countSubstrings(self, p: str) -> int:
        q = len(p)
        v = 0
        x = 0
        y = 0
        while x < q:
            y = 0
            z = 0
            while True:
                z = z * 10 + int(p[y + x])
                v = int(p[y + x])
                if v != 0 and (z % v) == 0:
                    # Repeated increments and decrements on v that don't affect logic are no-ops.
                    # They appear to have no effect, so ignored for functional equivalence.
                    y += 1
                if y >= q - x:
                    break
            x += 1

        w = v
        return (w - v) + v