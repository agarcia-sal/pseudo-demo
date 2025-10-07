class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        length = 1
        ops = []

        for op in param_operations:
            ops.append(op)
            # Both cases multiply length by two (same result)
            length *= 2

        char = 'a'

        for i in range(len(ops) - 1, -1, -1):
            half = length // 2
            if param_k <= half:
                length = half
            else:
                param_k -= half
                length = half
                if ops[i] == 1:
                    # shift char forward by one letter, wrapping around 'z' to 'a'
                    char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))

        return char