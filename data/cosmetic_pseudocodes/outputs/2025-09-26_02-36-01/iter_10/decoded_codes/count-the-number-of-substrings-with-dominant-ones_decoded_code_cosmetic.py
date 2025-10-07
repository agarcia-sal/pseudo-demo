class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        total = 0

        def CheckSegment(posA: int, posB: int, onesAccum: list, zerosAccum: list) -> None:
            if s[posB] == '1':
                onesAccum[0] += 1
            else:
                zerosAccum[0] += 1
            if onesAccum[0] >= zerosAccum[0] * zerosAccum[0]:
                nonlocal total
                total += 1

        def ExploreSegments(currIdx: int) -> None:
            if currIdx == n:
                return

            def Traverse(innerIdx: int, onesCount: list, zerosCount: list) -> None:
                if innerIdx == n:
                    return
                CheckSegment(currIdx, innerIdx, onesCount, zerosCount)
                Traverse(innerIdx + 1, onesCount, zerosCount)

            Traverse(currIdx, [0], [0])
            ExploreSegments(currIdx + 1)

        ExploreSegments(0)
        return total