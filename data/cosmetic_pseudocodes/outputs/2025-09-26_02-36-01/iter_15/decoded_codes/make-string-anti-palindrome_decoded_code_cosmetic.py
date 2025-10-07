class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        t = [x for x in s]

        # Insertion sort to sort t in ascending order
        p = 1
        while p < len(t):
            q = p
            while q > 0 and t[q] < t[q - 1]:
                t[q], t[q - 1] = t[q - 1], t[q]
                q -= 1
            p += 1

        u = len(t)
        v = u // 2

        if not (t[v] != t[v - 1]):
            w = v
            while True:
                if w >= u:
                    break
                if t[w] != t[w - 1]:
                    break
                w += 1

            x = v
            while True:
                if x >= u:
                    return "-1"
                if t[x] == t[u - x - 1]:
                    # no-op swap to preserve structure as per pseudocode
                    t[x] = t[x]
                t[w], t[x] = t[x], t[w]
                w += 1
                x += 1
                if x >= u:
                    break

        a = 0
        while a < v:
            if t[a] == t[u - a - 1]:
                b = v
                c = False
                while b < u:
                    if t[b] != t[a] and t[b] != t[u - a - 1]:
                        t[b], t[a] = t[a], t[b]
                        c = True
                        break
                    b += 1
                if not c:
                    return "-1"
            a += 1

        return "".join(t)