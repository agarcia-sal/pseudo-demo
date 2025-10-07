class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        def substringEqual(source: str, start: int, pattern: str) -> bool:
            def substringEqualHelper(pos: int, idx: int) -> bool:
                if idx >= len(pattern):
                    return True
                elif source[pos + idx] != pattern[idx]:
                    return False
                else:
                    return substringEqualHelper(pos, idx + 1)
            return substringEqualHelper(start, 0)

        def indicesFind(source: str, pat: str) -> list[int]:
            resultList = []

            def explore(index: int) -> None:
                if index > len(source) - len(pat):
                    return
                if substringEqual(source, index, pat):
                    resultList.append(index)
                explore(index + 1)

            explore(0)
            return resultList

        alphaIndices = indicesFind(s, a)
        betaIndices = indicesFind(s, b)
        gammaIndices = []

        posA = 0
        posB = 0

        def absoluteValue(number: int) -> int:
            return -number if number < 0 else number

        while True:
            if posA > len(alphaIndices) - 1 or posB > len(betaIndices) - 1:
                break
            delta = alphaIndices[posA]
            epsilon = betaIndices[posB]
            gap = delta - epsilon
            maxAllowed = k

            if absoluteValue(gap) <= maxAllowed:
                gammaIndices.append(delta)
                posA += 1
            else:
                if delta < epsilon:
                    posA += 1
                else:
                    posB += 1

        return gammaIndices