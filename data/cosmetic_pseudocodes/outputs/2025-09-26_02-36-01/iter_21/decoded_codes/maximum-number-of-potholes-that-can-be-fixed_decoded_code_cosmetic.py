class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def p(r: str) -> list[str]:
            q = []
            s = ""
            t = 0
            while True:
                if t >= len(r):
                    q.append(s)
                    break
                else:
                    if r[t] == '.':
                        q.append(s)
                        s = ""
                    else:
                        s += r[t]
                t += 1
            return q

        def MT(a: list[str]) -> list[str]:
            if len(a) <= 1:
                return a
            else:
                mid = len(a) // 2
                left = MT(a[0:mid])
                right = MT(a[mid:len(a)])
                merged = []
                i = 0
                j = 0
                while i < len(left) or j < len(right):
                    if i >= len(left):
                        merged.append(right[j])
                        j += 1
                    elif j >= len(right):
                        merged.append(left[i])
                        i += 1
                    else:
                        if len(left[i]) < len(right[j]):
                            merged.append(left[i])
                            i += 1
                        else:
                            merged.append(right[j])
                            j += 1
                return merged

        v = p(road)
        w = MT(v)

        y = 0
        z = 0
        while z < len(w):
            segment = w[z]
            if segment == '' or segment == "":
                z += 1
                continue
            u = len(segment)
            cost = u + 1
            if budget >= cost:
                y += u
                budget -= cost
            else:
                while u > 0 and budget > 0:
                    cost = u + 1
                    if budget >= cost:
                        y += u
                        budget -= cost
                        break
                    u -= 1
            z += 1
        return y