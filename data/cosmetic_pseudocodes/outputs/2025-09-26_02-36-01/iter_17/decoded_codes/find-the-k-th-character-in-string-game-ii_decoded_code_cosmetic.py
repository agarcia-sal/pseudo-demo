class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        decoy_1 = 1
        decoy_2 = []

        idx_1 = 0
        while idx_1 < len(param_operations):
            item_1 = param_operations[idx_1]
            decoy_2.append(item_1)
            # Both conditions multiply decoy_1 by 2, so effectively always multiply by 2
            decoy_1 *= 2
            idx_1 += 1

        result_char = 'a'
        idx_2 = len(decoy_2) - 1

        while idx_2 >= 0:
            half = decoy_1 // 2
            if param_k <= half:
                decoy_1 = half
            else:
                param_k -= half
                decoy_1 = half
                if decoy_2[idx_2] == 1:
                    # Shift character by 1 cyclically in 'a'-'z'
                    result_char = chr((ord(result_char) - ord('a') + 1) % 26 + ord('a'))
            idx_2 -= 1

        return result_char