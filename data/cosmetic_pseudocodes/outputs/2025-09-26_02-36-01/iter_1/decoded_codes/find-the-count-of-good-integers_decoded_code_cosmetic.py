class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fac = [1]
        for i in range(1, n + 1):
            fac.append(fac[i - 1] * i)

        ans = 0
        visited = set()
        half_len = (n - 1) // 2
        start_num = 10 ** half_len
        end_num = start_num * 10

        for num in range(start_num, end_num):
            str_num = str(num)
            rev_part = str_num[::-1][n % 2:]
            candidate = str_num + rev_part

            candidate_int = int(candidate)
            if candidate_int % k != 0:
                continue

            sorted_candidate = ''.join(sorted(candidate))
            if sorted_candidate in visited:
                continue
            visited.add(sorted_candidate)

            count_map = {}
            for ch in sorted_candidate:
                count_map[ch] = count_map.get(ch, 0) + 1

            if '0' in count_map and count_map['0'] > 0:
                res = (n - count_map['0']) * fac[n - 1]
            else:
                res = fac[n]

            for freq in count_map.values():
                res //= fac[freq]

            ans += res

        return ans