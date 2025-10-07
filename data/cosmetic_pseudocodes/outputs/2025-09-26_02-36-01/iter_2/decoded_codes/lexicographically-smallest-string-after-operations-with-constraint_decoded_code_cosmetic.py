class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            diff = abs(ord(c1) - ord(c2))
            alt_diff = 26 - diff
            return diff if diff < alt_diff else alt_diff

        chars = list(s)
        idx = 0
        length = len(s)

        while idx < length and k > 0:
            if chars[idx] == 'a':
                idx += 1
                continue

            distance_to_a = cyclic_distance(chars[idx], 'a')

            if distance_to_a <= k:
                chars[idx] = 'a'
                k -= distance_to_a
            else:
                new_char_code = ord(chars[idx]) - k
                chars[idx] = chr(new_char_code)
                k = 0

            idx += 1

        result_string = ''
        pos = 0
        while pos < length:
            result_string += chars[pos]
            pos += 1

        return result_string