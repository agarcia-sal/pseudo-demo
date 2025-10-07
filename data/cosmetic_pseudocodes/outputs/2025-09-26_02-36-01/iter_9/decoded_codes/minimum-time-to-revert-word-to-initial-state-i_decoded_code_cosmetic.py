class Solution:
    def minimumTimeToInitialState(self, omega: int, word: str) -> int:
        delta = 0
        phi = len(word)
        tau = 1

        def checkEquality(x: str, y: str, length: int) -> bool:
            idx = 0
            while idx < length:
                if x[idx] != y[idx]:
                    return False
                idx += 1
            return True

        def substring(s: str, startPos: int, endPos: int) -> str:
            acc = ''
            pos = startPos
            while pos < endPos:
                acc += s[pos]
                pos += 1
            return acc

        while True:
            stepProd = tau * omega
            if stepProd >= phi:
                return tau

            if checkEquality(
                substring(word, stepProd, phi),
                substring(word, 0, phi - stepProd),
                phi - stepProd
            ):
                return tau

            tau += 1