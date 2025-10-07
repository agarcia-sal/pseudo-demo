class Solution:
    def validStrings(self, n: int) -> list[str]:
        output_collection = []

        def helperSequence(seq: str) -> None:
            if len(seq) >= n:
                output_collection.append(seq)
                return
            last_char = seq[-1]
            if last_char == "1":
                helperSequence(seq + "0")
                helperSequence(seq + "1")
            elif last_char == "0":
                helperSequence(seq + "1")

        if n == 1:
            return ["0", "1"]

        helperSequence("0")
        helperSequence("1")

        return output_collection