class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        factorials = []
        for idx in range(n + 1):
            curr_factorial = 1
            for mul in range(1, idx + 1):
                curr_factorial *= mul
            factorials.append(curr_factorial)

        total = 0
        seenCombinations = set()
        half_base = 1
        exp = (n - 1) // 2
        for _ in range(exp):
            half_base *= 10

        start_val = half_base
        end_val = half_base * 10 - 1
        curr = start_val
        while curr <= end_val:
            num_str = str(curr)
            rem = n % 2
            reversed_part = ""
            rev_idx = len(num_str) - 1 - rem
            while rev_idx >= 0:
                reversed_part += num_str[rev_idx]
                rev_idx -= 1
            palindrome_str = num_str + reversed_part

            palindrome_num = int(palindrome_str)
            if palindrome_num % k != 0:
                curr += 1
                continue

            sorted_chars = sorted(palindrome_str)
            sorted_str = "".join(sorted_chars)

            if sorted_str in seenCombinations:
                curr += 1
                continue
            seenCombinations.add(sorted_str)

            freq_map = {}
            for ch in sorted_chars:
                freq_map[ch] = freq_map.get(ch, 0) + 1

            if '0' in freq_map and freq_map['0'] > 0:
                zero_count = freq_map['0']
                res_val = (n - zero_count) * factorials[n - 1]
            else:
                res_val = factorials[n]

            for cnt_val in freq_map.values():
                res_val //= factorials[cnt_val]

            total += res_val
            curr += 1

        return total