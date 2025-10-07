class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        list_X = []
        m = 0
        n = len(s) - len(a)
        while True:
            if m > n:
                break
            temp_sub = s[m : m + len(a)]
            if temp_sub == a:
                list_X.append(m)
            m += 1

        list_Y = []
        p = 0
        q = len(s) - len(b)
        while True:
            if p > q:
                break
            temp_sub2 = s[p : p + len(b)]
            if temp_sub2 == b:
                list_Y.append(p)
            p += 1

        resultList = []
        alpha = 0
        beta = 0
        while True:
            if alpha >= len(list_X) or beta >= len(list_Y):
                break
            dist = abs(list_X[alpha] - list_Y[beta])
            if dist <= k:
                resultList.append(list_X[alpha])
                alpha += 1
            else:
                if list_X[alpha] < list_Y[beta]:
                    alpha += 1
                else:
                    beta += 1
        return resultList