class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            absDiff = abs(ord(c1) - ord(c2))
            complement = 26 - absDiff
            return complement if complement < absDiff else absDiff

        charArray = list(s)
        lengthStr = len(s)
        pos = 0

        while k > 0 and pos < lengthStr:
            if charArray[pos] == 'a':
                pos += 1
                continue

            distA = cyclic_distance(charArray[pos], 'a')
            if distA <= k:
                charArray[pos] = 'a'
                k -= distA
            else:
                charArray[pos] = chr(ord(charArray[pos]) - k)
                k = 0
            pos += 1

        return ''.join(charArray)