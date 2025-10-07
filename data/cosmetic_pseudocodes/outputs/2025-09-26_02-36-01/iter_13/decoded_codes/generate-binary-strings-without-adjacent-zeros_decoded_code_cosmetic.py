class Solution:
    def validStrings(self, n: int) -> list[str]:
        results = []

        def recurse(sequence: str) -> None:
            if len(sequence) == n:
                results.append(sequence)
                return
            last_char = sequence[-1]
            if last_char == "1":
                recurse(sequence + "0")
                recurse(sequence + "1")
            elif last_char == "0":
                recurse(sequence + "1")

        if n == 1:
            return ["0", "1"]
        recurse("0")
        recurse("1")
        return results