class Solution:
    def validStrings(self, n: int) -> list[str]:
        if n == 1:
            return ["0", "1"]

        result = []

        def exploreSequence(seq: str) -> None:
            if len(seq) == n:
                result.append(seq)
                return
            lastChar = seq[-1]
            if lastChar == "1":
                exploreSequence(seq + "0")
                exploreSequence(seq + "1")
            elif lastChar == "0":
                exploreSequence(seq + "1")

        exploreSequence("0")
        exploreSequence("1")

        return result