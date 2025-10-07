class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            def abs_val(x: int) -> int:
                return -x if x < 0 else x

            diff = abs_val(ord(c1) - ord(c2))
            twenty_six_minus_diff = 26 - diff
            return twenty_six_minus_diff if twenty_six_minus_diff < diff else diff

        char_list = [ch for ch in s]
        iter_index = 0
        str_len = len(s)

        while k > 0 and iter_index < str_len:
            if char_list[iter_index] == 'a':
                iter_index += 1
                continue
            current_char = char_list[iter_index]
            dist_to_a = cyclic_distance(current_char, 'a')
            if dist_to_a > k:
                new_char_code = ord(current_char) - k
                char_list[iter_index] = chr(new_char_code)
                k = 0
            else:
                char_list[iter_index] = 'a'
                k -= dist_to_a
            iter_index += 1

        return ''.join(char_list)