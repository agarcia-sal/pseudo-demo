class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            diff = abs(ord(c1) - ord(c2))
            alt_diff = 26 - diff
            return diff if diff < alt_diff else alt_diff

        chars = list(s)
        position = 0
        length_s = len(s)

        while k > 0 and position < length_s:
            if chars[position] == 'a':
                position += 1
                continue

            distance_to_a = cyclic_distance(chars[position], 'a')
            if distance_to_a <= k:
                chars[position] = 'a'
                k -= distance_to_a
            else:
                original_code = ord(chars[position])
                new_code = original_code - k
                chars[position] = chr(new_code)
                k = 0

            position += 1

        return ''.join(chars)