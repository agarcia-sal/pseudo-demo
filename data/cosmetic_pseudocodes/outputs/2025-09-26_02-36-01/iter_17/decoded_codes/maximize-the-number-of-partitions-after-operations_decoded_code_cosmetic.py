class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            u = 0
            v = set()
            idx = 0
            while idx < len(s):
                c = s[idx]
                if len(v) < k:
                    v.add(c)
                else:
                    if c in v:
                        pass
                    else:
                        u += 1
                        v = {c}
                idx += 1
            if len(v) > 0:
                u += 1
            return u

        r = max_partitions(s, k)
        p = 0
        while p < len(s):
            for x in (chr(c) for c in range(ord('a'), ord('z') + 1)):
                if x == s[p]:
                    continue
                t = ""
                if p > 0:
                    t += s[:p]
                t += x
                if p + 1 < len(s):
                    t += s[p+1:]
                w = max_partitions(t, k)
                if w > r:
                    r = w
            p += 1
        return r