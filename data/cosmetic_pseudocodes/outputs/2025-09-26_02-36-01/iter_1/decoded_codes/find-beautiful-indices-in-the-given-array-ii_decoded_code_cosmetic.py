class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        positionsOfA = []
        maxStartA = len(s) - len(a)
        for pos in range(maxStartA + 1):
            if s[pos:pos+len(a)] == a:
                positionsOfA.append(pos)

        positionsOfB = []
        maxStartB = len(s) - len(b)
        for pos in range(maxStartB + 1):
            if s[pos:pos+len(b)] == b:
                positionsOfB.append(pos)

        resultIndices = []
        pointerA, pointerB = 0, 0

        while pointerA < len(positionsOfA) and pointerB < len(positionsOfB):
            diff = abs(positionsOfA[pointerA] - positionsOfB[pointerB])
            if diff <= k:
                resultIndices.append(positionsOfA[pointerA])
                pointerA += 1
            elif positionsOfA[pointerA] < positionsOfB[pointerB]:
                pointerA += 1
            else:
                pointerB += 1

        return resultIndices