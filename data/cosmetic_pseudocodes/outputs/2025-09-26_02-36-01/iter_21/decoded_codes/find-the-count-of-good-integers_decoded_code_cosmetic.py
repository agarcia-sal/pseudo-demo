class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def computeFactorial(y: int) -> int:
            if y <= 1:
                return 1
            else:
                return y * computeFactorial(y - 1)

        u = []
        p = 0
        while p < n + 1:
            u.append(computeFactorial(p))
            p += 1

        z = 0
        w = set()

        q = 1
        r = n - 1
        o = r // 2

        v = q
        while o > 0:
            v *= 10
            o -= 1

        m = v
        while m < v * 10:
            a = str(m)
            rev_str = a[::-1]

            cnt_sub = n % 2

            b = a + rev_str[cnt_sub:]

            c = int(b)
            if c % k != 0:
                m += 1
                continue

            ch_list = list(b)
            ch_list.sort()
            tmp = ''.join(ch_list)
            if tmp in w:
                m += 1
                continue
            w.add(tmp)

            freq = {}
            for ch in tmp:
                freq[ch] = freq.get(ch, 0) + 1

            if "0" in freq and freq["0"] > 0:
                sub_val = n - freq["0"]
                res = sub_val * u[n - 1]
            else:
                res = u[n]

            for val in freq.values():
                res //= u[val]

            z += res
            m += 1

        return z