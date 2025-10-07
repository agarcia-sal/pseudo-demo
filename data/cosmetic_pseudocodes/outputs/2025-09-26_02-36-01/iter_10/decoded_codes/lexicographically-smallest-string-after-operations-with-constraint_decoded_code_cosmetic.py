class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            x = abs(ord(c1) - ord(c2))
            return min(x, 26 - x)

        arr = list(s)
        pos = 0
        length = len(s)

        while k > 0 and pos < length:
            if arr[pos] == 'a':
                pos += 1
                continue

            dist = cyclic_distance(arr[pos], 'a')
            if dist <= k:
                arr[pos] = 'a'
                k -= dist
            else:
                arr[pos] = chr(ord(arr[pos]) - k)
                k = 0
            pos += 1

        return "".join(arr)