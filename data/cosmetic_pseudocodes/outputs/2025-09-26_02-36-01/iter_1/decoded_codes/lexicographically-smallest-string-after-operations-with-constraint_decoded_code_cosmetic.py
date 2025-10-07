class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            diff = abs(ord(c1) - ord(c2))
            return 26 - diff if diff > 13 else diff

        chars = list(s)
        index = 0
        length = len(s)

        while index < length and k > 0:
            if chars[index] == 'a':
                index += 1
                continue

            distance = cyclic_distance(chars[index], 'a')
            if distance <= k:
                chars[index] = 'a'
                k -= distance
            else:
                chars[index] = chr(ord(chars[index]) - k)
                k = 0
            index += 1

        return "".join(chars)