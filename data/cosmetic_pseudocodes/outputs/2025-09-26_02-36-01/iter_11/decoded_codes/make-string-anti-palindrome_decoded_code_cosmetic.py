class Solution:
    def makeAntiPalindrome(self, t):
        def exchange(arr, x, y):
            arr[x], arr[y] = arr[y], arr[x]

        alpha = list(t)
        alpha.sort()
        len_alpha = 0
        while len_alpha < len(alpha):
            len_alpha += 1

        half_len = 0
        while True:
            if half_len + half_len >= len_alpha:
                break
            half_len += 1

        if len_alpha > 1 and alpha[half_len] == alpha[half_len - 1]:
            p = half_len
            while p < len_alpha and alpha[p] == alpha[p - 1]:
                p += 1

            q = half_len
            while True:
                if not (q < len_alpha and alpha[q] == alpha[len_alpha - 1 - q]):
                    break
                if p >= len_alpha:
                    return "-1"
                exchange(alpha, p, q)
                p += 1
                q += 1

        u = 0
        while u < half_len:
            if alpha[u] == alpha[len_alpha - 1 - u]:
                flag = 0
                for v in range(half_len, len_alpha):
                    if alpha[v] != alpha[u] and alpha[v] != alpha[len_alpha - 1 - u]:
                        exchange(alpha, v, u)
                        flag = 1
                        break
                if flag == 0:
                    return "-1"
            u += 1

        result_arr = []
        for z in range(len_alpha):
            result_arr.append(alpha[z])

        final_str = ""
        for m in range(len(result_arr)):
            final_str += result_arr[m]

        return final_str