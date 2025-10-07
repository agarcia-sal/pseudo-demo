class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        q1 = 0
        q2 = len(s)
        q3 = len(a)
        q4 = 0
        q5 = []
        while q4 <= q2 - q3:
            if s[q4:q4 + q3] == a:
                q5.append(q4)
            q4 += 1

        q6 = len(b)
        q7 = []
        q8 = 0
        while q8 <= q2 - q6:
            if s[q8:q8 + q6] == b:
                q7.append(q8)
            q8 += 1

        q9 = []
        q10 = 0
        while q10 < len(q5):
            q11 = 0
            flag = False
            while (not flag) and (q11 < len(q7)):
                if abs(q5[q10] - q7[q11]) <= k:
                    q9.append(q5[q10])
                    flag = True
                q11 += 1
            q10 += 1

        return q9