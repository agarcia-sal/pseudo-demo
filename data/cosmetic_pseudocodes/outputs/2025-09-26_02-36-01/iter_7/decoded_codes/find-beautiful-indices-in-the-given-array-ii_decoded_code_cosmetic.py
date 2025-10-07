class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        length_s = len(s)
        length_a = len(a)
        length_b = len(b)

        def collectPositions(substr: str, substr_len: int) -> list[int]:
            positions = []
            pos = 0
            while pos <= length_s - substr_len:
                if s[pos : pos + substr_len] == substr:
                    positions.append(pos)
                pos += 1
            return positions

        posA = collectPositions(a, length_a)
        posB = collectPositions(b, length_b)

        resIndices = []

        def absValue(x: int) -> int:
            return x if x >= 0 else -x

        ix = 0
        jx = 0
        while ix < len(posA) and jx < len(posB):
            diff = absValue(posA[ix] - posB[jx])
            if diff <= k:
                resIndices.append(posA[ix])
                ix += 1
            elif posA[ix] < posB[jx]:
                ix += 1
            else:
                jx += 1

        return resIndices