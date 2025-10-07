class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        o = 0
        p = len(word)
        q = []
        while o < p:
            r = word[o:o + k]
            q.append(r)
            o += k
        s = {}
        for t in q:
            if t not in s:
                s[t] = 0
            s[t] += 1
        u = 0
        for v in s:
            if s[v] > u:
                u = s[v]
        w = len(q) - u
        return w