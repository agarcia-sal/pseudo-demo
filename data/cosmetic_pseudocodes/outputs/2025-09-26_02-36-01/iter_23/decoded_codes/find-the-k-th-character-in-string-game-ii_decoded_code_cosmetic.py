class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"

        def charShift(c: str) -> str:
            idx = alpha.index(c)
            newIndex = (idx + 1) % len(alpha)
            return alpha[newIndex]

        # appendOps simply copies inputOps to outputOps recursively
        # Replace with direct copy to avoid recursion overhead
        all_ops = list(param_operations)

        # updateLength doubles the length per each operation
        # Simplify iterative computation instead of recursion
        a_length = 1
        for op in all_ops:
            # The provided pseudocode doubles length regardless of op value
            a_length *= 2
        len_result = a_length

        resultChar = "a"

        def decodeRecursive(pos: int, kVal: int, currLen: int, opsList: list[int], finalChar: str) -> str:
            if pos < 0:
                return finalChar
            halfLen = currLen // 2
            if kVal <= halfLen:
                return decodeRecursive(pos - 1, kVal, halfLen, opsList, finalChar)
            else:
                newK = kVal - halfLen
                if opsList[pos] == 1:
                    updatedChar = charShift(finalChar)
                else:
                    updatedChar = finalChar
                return decodeRecursive(pos - 1, newK, halfLen, opsList, updatedChar)

        decoded = decodeRecursive(len(all_ops) - 1, param_k, len_result, all_ops, resultChar)
        return decoded