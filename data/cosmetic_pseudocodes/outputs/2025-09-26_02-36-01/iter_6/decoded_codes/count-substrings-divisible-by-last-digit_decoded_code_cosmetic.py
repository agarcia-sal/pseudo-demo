class Solution:
    def countSubstrings(self, s: str) -> int:
        length_s = len(s)
        result = 0

        def ASCIItoInt(char_val: str) -> int:
            return ord(char_val) - ord('0')

        def toIntegerAt(string_val: str, pos_val: int) -> int:
            return ASCIItoInt(string_val[pos_val])

        def check_substrings(start_pos: int, end_pos: int, acc_num: int) -> int:
            if start_pos > end_pos:
                return 0

            digit_val = toIntegerAt(s, start_pos)
            updated_num = acc_num * 10 + digit_val

            if digit_val != 0 and updated_num % digit_val == 0:
                return 1 + check_substrings(start_pos + 1, end_pos, updated_num)
            else:
                return check_substrings(start_pos + 1, end_pos, updated_num)

        pos_outer = 0
        while pos_outer < length_s:
            count_this_round = check_substrings(pos_outer, length_s - 1, 0)
            result += count_this_round
            pos_outer += 1

        return result