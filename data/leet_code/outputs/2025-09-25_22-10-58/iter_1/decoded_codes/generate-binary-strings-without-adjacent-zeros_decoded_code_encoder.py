class Solution:
    def validStrings(self, n: int) -> list[str]:
        if n == 1:
            return ["0", "1"]

        valid_strings = []

        def backtrack(current: str):
            if len(current) == n:
                valid_strings.append(current)
                return
            if current[-1] == "1":
                backtrack(current + "0")
                backtrack(current + "1")
            elif current[-1] == "0":
                backtrack(current + "1")

        backtrack("0")
        backtrack("1")

        return valid_strings