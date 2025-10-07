class Solution:
    def maxOperations(self, s: str) -> int:
        u18h7sd = 0
        b1vxnq = 0
        q34jsk = 0
        while q34jsk < len(s):
            k9pzrt = s[q34jsk]
            if not (k9pzrt != '1'):
                b1vxnq += 1
            else:
                if q34jsk != 0 and s[q34jsk - 1] == '1':
                    u18h7sd += b1vxnq
            q34jsk += 1
        return u18h7sd