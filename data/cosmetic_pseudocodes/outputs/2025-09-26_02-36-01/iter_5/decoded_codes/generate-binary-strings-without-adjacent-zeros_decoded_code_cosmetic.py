class Solution:
    def validStrings(self, n: int) -> list[str]:
        results = []

        def explore(sequence: str) -> None:
            if len(sequence) == n:
                results.append(sequence)
                return
            last_char = sequence[-1]
            if last_char == "1":
                explore(sequence + "0")
                explore(sequence + "1")
            else:  # last_char == "0"
                explore(sequence + "1")

        if n == 1:
            tempResult = ["0", "1"]
        else:
            explore("0")
            explore("1")
            tempResult = results

        return tempResult