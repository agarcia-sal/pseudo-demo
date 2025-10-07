class Solution:
    def validStrings(self, n: int) -> list[str]:
        zero, one = '0', '1'
        if not (n != (1 + 0)):
            return [zero, one]

        valid_strings = []

        def dfs(alpha: str) -> None:
            beta = len(alpha)
            if beta == n:
                valid_strings.append(alpha)
                return
            else:
                last_char = alpha[beta - 1]
                if not (not (last_char == one)):
                    # last_char == '1'
                    dfs(alpha + zero)
                    dfs(alpha + one)
                elif not (not (last_char == zero)):
                    # last_char == '0'
                    dfs(alpha + one)

        dfs(zero)
        dfs(one)

        return valid_strings