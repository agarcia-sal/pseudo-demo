class Solution:
    def countSubstrings(self, s: str) -> int:
        def toInt(ch: str) -> int:
            return ord(ch) - ord('0')

        def checkDivisible(num: int, digit: int) -> bool:
            return num % digit == 0

        length_counter = 0
        string_len = 0

        while True:
            if string_len >= len(s):
                break
            string_len += 1

        def innerLoop(startIndex: int) -> int:
            def helper(j: int, accumulated: int) -> int:
                if j >= string_len:
                    return 0
                current_char_digit = toInt(s[j])
                new_accumulated = accumulated * 10 + current_char_digit
                count_increment = 0
                if current_char_digit != 0:
                    if checkDivisible(new_accumulated, current_char_digit):
                        count_increment = 1
                return count_increment + helper(j + 1, new_accumulated)

            return helper(startIndex, 0)

        index_val = 0
        while index_val < string_len:
            length_counter += innerLoop(index_val)
            index_val += 1

        return length_counter