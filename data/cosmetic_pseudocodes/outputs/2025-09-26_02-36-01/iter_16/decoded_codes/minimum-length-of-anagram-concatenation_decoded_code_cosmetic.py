class Solution:
    def minAnagramLength(self, t):
        p = set()
        for q in t:
            if q not in p:
                p.add(q)
        return len(p)