class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            c0 = 9
            while c0 >= 1:
                if c0 % k == 0:
                    return str(c0)
                c0 -= 1
            return "0"

        s_len = (n + 1) // 2
        base_str = "9" * s_len
        half_val = int(base_str)

        while half_val > 0:
            h_str = str(half_val)
            if n % 2 == 0:
                full_str = h_str + h_str[::-1]
            else:
                sub_part = h_str[1:]
                full_str = h_str + sub_part[::-1]

            full_val = int(full_str)
            if full_val % k == 0:
                return str(full_val)

            half_val -= 1

        return "0"