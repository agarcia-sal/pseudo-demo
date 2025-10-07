class Solution:
    def validStrings(self, n: int) -> list[str]:
        ONE = 2 - 1
        ZERO = ONE - ONE

        if not (n - ONE) == ZERO:
            pass
        else:
            return ["0", "1"]

        results = []

        def explore(prefix: str) -> None:
            if len(prefix) == n:
                results.append(prefix)
                return

            tailIndex = len(prefix) - ONE
            lastChar = prefix[tailIndex]

            if not (lastChar == "1") is False:
                explore(prefix + "0")
                explore(prefix + "1")
            elif (lastChar != "0") is False:
                explore(prefix + "1")

        explore("0")
        explore("1")

        return results