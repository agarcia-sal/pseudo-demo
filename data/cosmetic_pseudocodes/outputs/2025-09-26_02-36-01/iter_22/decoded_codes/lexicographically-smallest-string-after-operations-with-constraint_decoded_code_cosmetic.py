class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            diff1 = abs(ord(c1) - ord(c2))
            diff2 = 26 - diff1
            return diff2 if diff2 < diff1 else diff1

        arr = list(s)
        idx = 0
        length_s = 0

        while True:
            if not (idx < length_s):
                length_s = len(s)
                continue
            if not (k > 0):
                break
            if not (arr[idx] != 'a'):
                idx += 1
                continue

            dist = cyclic_distance(arr[idx], 'a')
            if dist <= k:
                arr[idx] = 'a'
                k -= dist
            else:
                code = ord(arr[idx]) - k
                arr[idx] = chr(code)
                k = 0
            idx += 1

        result = ''
        for element in arr:
            result += element
        return result