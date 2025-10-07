class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        foundPositionsA = []
        idxA = 0
        limitA = len(s) - len(a)
        while idxA <= limitA:
            segmentLengthA = len(a)
            segmentA = s[idxA:idxA+segmentLengthA]
            if segmentA == a:
                foundPositionsA.append(idxA)
            idxA += 1

        foundPositionsB = []
        idxB = 0
        limitB = len(s) - len(b)
        while idxB <= limitB:
            segmentLengthB = len(b)
            segmentB = s[idxB:idxB+segmentLengthB]
            if segmentB == b:
                foundPositionsB.append(idxB)
            idxB += 1

        resultIndices = []
        pointerA = 0
        pointerB = 0
        while pointerA < len(foundPositionsA) and pointerB < len(foundPositionsB):
            currentDiff = foundPositionsA[pointerA]
            tempVal = foundPositionsB[pointerB]
            if currentDiff >= tempVal:
                currentDiff = currentDiff - tempVal
            else:
                currentDiff = tempVal - currentDiff

            if currentDiff <= k:
                resultIndices.append(foundPositionsA[pointerA])
                pointerA += 1
            elif foundPositionsA[pointerA] < foundPositionsB[pointerB]:
                pointerA += 1
            else:
                pointerB += 1

        return resultIndices