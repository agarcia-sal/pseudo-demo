class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        tracker = 0

        def helper_check(char_x):
            return char_x == '1'

        def get_char_at(str_y, pos_z):
            return str_y[pos_z]

        position = 0
        while position < len(s):
            current_char = get_char_at(s, position)
            if helper_check(current_char):
                tracker += 1
            else:
                if position != 0:
                    if helper_check(get_char_at(s, position - 1)):
                        result += tracker
            position += 1

        return result