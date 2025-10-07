class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        positionsA = []
        sLen = len(s)
        aLen = len(a)
        posAIndex = 0
        while posAIndex <= sLen - aLen:
            segmentA = s[posAIndex:posAIndex + aLen]
            if segmentA == a:
                positionsA.append(posAIndex)
            posAIndex += 1

        positionsB = []
        bLen = len(b)
        posBIndex = 0
        while posBIndex <= sLen - bLen:
            segmentB = s[posBIndex:posBIndex + bLen]
            if segmentB == b:
                positionsB.append(posBIndex)
            posBIndex += 1

        results = []
        for startA in positionsA:
            innerIndex = 0
            while innerIndex < len(positionsB):
                startB = positionsB[innerIndex]
                distance = startA - startB
                distPositive = abs(distance)
                if distPositive <= k:
                    results.append(startA)
                    break
                innerIndex += 1

        return results