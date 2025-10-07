class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            val = 9
            while val >= 1:
                if val % k == 0:
                    return str(val)
                val -= 1
            return "0"

        half_len = (n + 1) // 2
        nine_str = ""
        count = 0
        while count < half_len:
            nine_str += "9"
            count += 1
        half = int(nine_str)

        while half > 0:
            half_str = str(half)
            if n % 2 == 0:
                rev_half_str = half_str[::-1]
                full_str = half_str + rev_half_str
            else:
                rev_sub_str = half_str[:-1][::-1]
                full_str = half_str + rev_sub_str

            full = int(full_str)
            if full % k == 0:
                return str(full)
            half -= 1

        return "0"