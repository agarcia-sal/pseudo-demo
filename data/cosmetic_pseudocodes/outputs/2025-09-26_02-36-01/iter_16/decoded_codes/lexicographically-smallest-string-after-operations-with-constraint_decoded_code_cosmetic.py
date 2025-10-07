class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            diff = abs(ord(c1) - ord(c2))
            complement = 26 - diff
            return diff if diff < complement else complement

        m = 0
        length_s = len(s)
        array_chars = list(s)

        while k > 0 and m < length_s:
            if array_chars[m] == 'a':
                m += 1
                continue

            diff_a = cyclic_distance(array_chars[m], 'a')

            if diff_a <= k:
                array_chars[m] = 'a'
                k -= diff_a
            else:
                old_char_code = ord(array_chars[m])
                new_char_code = old_char_code - k
                array_chars[m] = chr(new_char_code)
                k = 0

            m += 1

        return "".join(array_chars)