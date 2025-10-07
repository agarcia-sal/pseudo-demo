class Solution:
    def minStartingIndex(self, inputString: str, pattern: str) -> int:
        def is_almost_equal(subStr: str, pat: str) -> bool:
            mismatchCounter = 0

            def checkMismatch(pos: int) -> bool:
                nonlocal mismatchCounter
                if pos == len(subStr):
                    return True
                if subStr[pos] != pat[pos]:
                    mismatchCounter += 1
                    if mismatchCounter > 1:
                        return False
                return checkMismatch(pos + 1)

            return checkMismatch(0)

        patLen = len(pattern)
        resultIndex = -1

        def search(i: int):
            nonlocal resultIndex
            if i >= len(inputString) - patLen + 1:
                return
            if is_almost_equal(inputString[i : i + patLen], pattern):
                resultIndex = i
                return
            search(i + 1)

        search(0)
        return resultIndex