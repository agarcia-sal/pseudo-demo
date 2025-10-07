class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        list_x = []
        m = 0
        len_s = len(s)
        len_a = len(a)
        while True:
            if m > len_s - len_a:
                break
            temp_1 = s[m:m+len_a]
            if temp_1 == a:
                list_x.append(m)
            m += 1

        list_y = []
        n = 0
        len_b = len(b)
        while True:
            if n > len_s - len_b:
                break
            temp_2 = s[n:n+len_b]
            if temp_2 == b:
                list_y.append(n)
            n += 1

        result_list = []
        p = 0
        q = 0
        len_x = len(list_x)
        len_y = len(list_y)
        while p < len_x:
            if q >= len_y:
                break
            diff_val = abs(list_x[p] - list_y[q])
            if diff_val <= k:
                result_list.append(list_x[p])
                p += 1
            else:
                if list_x[p] < list_y[q]:
                    p += 1
                else:
                    q += 1

        return result_list