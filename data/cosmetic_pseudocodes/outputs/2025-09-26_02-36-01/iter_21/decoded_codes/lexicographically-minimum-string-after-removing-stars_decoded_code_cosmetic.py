class Solution:
    def clearStars(self, s: str) -> str:
        b = []
        a = 0
        while a < len(s):
            c = s[a]
            if c == '*':
                if b:
                    b.pop()
            else:
                b.append(c)
            a += 1

        def buildString(e: int, f: int) -> str:
            if e >= len(b):
                return ""
            return b[e] + buildString(e + 1, f)

        d = buildString(0, 0)
        return d