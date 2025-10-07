class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        locsA = []
        limitA = len(s) - len(a)
        posA = 0
        while posA <= limitA:
            if s[posA:posA + len(a)] == a:
                locsA.append(posA)
            posA += 1

        locsB = []
        limitB = len(s) - len(b)
        posB = 0
        while posB <= limitB:
            if s[posB:posB + len(b)] == b:
                locsB.append(posB)
            posB += 1

        resultIndices = []
        idxA = 0
        idxB = 0
        while idxA < len(locsA) and idxB < len(locsB):
            delta = locsA[idxA] - locsB[idxB]
            distance = abs(delta)
            if distance <= k:
                resultIndices.append(locsA[idxA])
                idxA += 1
            elif locsA[idxA] < locsB[idxB]:
                idxA += 1
            else:
                idxB += 1

        return resultIndices