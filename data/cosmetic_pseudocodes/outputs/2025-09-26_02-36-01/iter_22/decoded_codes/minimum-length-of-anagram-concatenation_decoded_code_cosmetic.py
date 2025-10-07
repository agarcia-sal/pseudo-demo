class Solution:
    def minAnagramLength(self, q):
        b = set()
        e = 0
        p = len(q)
        while e < p:
            if q[e] not in b:
                b.add(q[e])
            e += 1
        return len(b)