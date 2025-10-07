class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        size = 1
        opsList = []
        idx = 0
        while idx < len(param_operations):
            current_op = param_operations[idx]
            opsList.append(current_op)
            # Size doubles regardless of current_op according to the pseudocode
            size += size
            idx += 1

        resultChar = 'a'
        pos = len(opsList) - 1
        while pos >= 0:
            half = size // 2
            if param_k <= half:
                size = half
            else:
                param_k -= half
                size = half
                if opsList[pos] == 1:
                    incremented_val = ord(resultChar) + 1
                    if incremented_val > ord('z'):
                        incremented_val = ord('a')
                    resultChar = chr(incremented_val)
            pos -= 1

        return resultChar