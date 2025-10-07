class Solution:
    def validStrings(self, n: int) -> list[str]:
        valid_strings = []

        def backtrack(current_string: str) -> None:
            length_current = len(current_string)
            if length_current == n:
                valid_strings.append(current_string)
                return

            last_char = current_string[-1]

            if last_char == "1":
                backtrack(current_string + "0")
                backtrack(current_string + "1")
            elif last_char == "0":
                backtrack(current_string + "1")

        if n == 1:
            return ["0", "1"]

        backtrack("0")
        backtrack("1")

        return valid_strings