class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            delta = abs(ord(c1) - ord(c2))
            diff = 26 - delta
            return delta if delta <= diff else diff

        char_array = list(s)
        idx = 0
        length_s = len(s)

        while k > 0 and idx < length_s:
            if char_array[idx] == 'a':
                idx += 1
                continue

            dist = cyclic_distance(char_array[idx], 'a')

            if dist <= k:
                char_array[idx] = 'a'
                k -= dist
            else:
                char_array[idx] = chr(ord(char_array[idx]) - k)
                k = 0
            idx += 1

        return ''.join(char_array)