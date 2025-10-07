class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        def nextChar(ch: str) -> str:
            base = ord('a')
            code = ord(ch)
            return chr(base + (code - base + 1) % 26)

        def doubleLength(val: int, length: int) -> int:
            # According to pseudocode: length doubles for every operation regardless of val
            return length * 2

        alpha = 'a'
        count = 1
        sequence = []

        idx = 0
        while idx < len(param_operations):
            current = param_operations[idx]
            sequence.append(current)
            count = doubleLength(current, count)
            idx += 1

        position = len(sequence) - 1
        while position >= 0:
            half = count // 2
            if param_k <= half:
                count = half
            else:
                param_k -= half
                count = half
                if sequence[position] == 1:
                    alpha = nextChar(alpha)
            position -= 1

        return alpha