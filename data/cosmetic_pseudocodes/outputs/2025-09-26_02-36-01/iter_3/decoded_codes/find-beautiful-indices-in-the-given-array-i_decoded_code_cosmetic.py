class Solution:
    def beautifulIndices(self, s, a, b, k):
        posA = []
        lenS = len(s)
        lenA = len(a)
        start = 0
        while start <= lenS - lenA:
            segment = s[start:start+lenA]
            if segment == a:
                posA.append(start)
            start += 1

        posB = []
        lenB = len(b)
        ptr = 0
        while ptr <= lenS - lenB:
            fragment = s[ptr:ptr+lenB]
            if fragment == b:
                posB.append(ptr)
            ptr += 1

        resultIndices = []
        for valX in posA:
            for valY in posB:
                diff = abs(valX - valY)
                if diff <= k:
                    resultIndices.append(valX)
                    break

        return resultIndices