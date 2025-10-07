class Solution:
    def validStrings(self, length: int) -> list[str]:
        if length == 1:
            return ["0", "1"]

        validSequences = []

        def backtrack(sequence: str) -> None:
            if len(sequence) == length:
                validSequences.append(sequence)
                return

            lastChar = sequence[-1]
            if lastChar == "1":
                backtrack(sequence + "0")
                backtrack(sequence + "1")
            elif lastChar == "0":
                backtrack(sequence + "1")

        backtrack("0")
        backtrack("1")

        return validSequences