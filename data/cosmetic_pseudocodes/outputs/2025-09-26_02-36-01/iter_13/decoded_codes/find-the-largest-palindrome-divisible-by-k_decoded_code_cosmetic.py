class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        result_string = "0"
        is_odd_length = (n % 2) != 0
        max_digit = 9
        one_val = 1
        nine_string = "9"
        two_val = 2
        zero = 0

        if n == one_val:
            current_num = max_digit
            while current_num >= one_val:
                if current_num % k == 0:
                    result_string = str(current_num)
                    return result_string
                current_num -= one_val
            return result_string

        def reverse_string(input_str: str) -> str:
            reversed_str = ""
            index = len(input_str) - one_val
            while index >= zero:
                reversed_str += input_str[index]
                index -= one_val
            return reversed_str

        def substring(input_str: str, start_idx: int, end_idx: int) -> str:
            sub_str = ""
            idx = start_idx
            while idx <= end_idx:
                sub_str += input_str[idx]
                idx += one_val
            return sub_str

        def concat_string_times(char_str: str, times: int) -> str:
            res = ""
            counter = 0
            while counter < times:
                res += char_str
                counter += one_val
            return res

        def int_parse(str_val: str) -> int:
            return int(str_val)

        length_half = (n + one_val) // two_val
        nine_repeated = concat_string_times(nine_string, length_half)
        half_val = int_parse(nine_repeated)

        while half_val > 0:
            half_str = str(half_val)
            if not is_odd_length:
                palindrome_str = half_str + reverse_string(half_str)
            else:
                inner_substring = substring(half_str, zero, len(half_str) - two_val)
                palindrome_str = half_str + reverse_string(inner_substring)
            palindrome_num = int_parse(palindrome_str)
            if palindrome_num % k == 0:
                return palindrome_str
            half_val -= one_val

        return result_string