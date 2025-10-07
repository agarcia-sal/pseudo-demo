class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        idx_a = 97
        len_var = 1
        ops_list = []

        m = 0
        while m < len(param_operations):
            current_op = param_operations[m]
            ops_list.append(current_op)
            len_var *= 2
            m += 1

        result_char_code = idx_a
        j = len(ops_list) - 1

        while j >= 0:
            half = len_var // 2
            if param_k <= half:
                len_var = half
            else:
                param_k -= half
                len_var = half
                if ops_list[j] == 1:
                    # shift character by 1 modulo 26
                    result_char_code = ((result_char_code - idx_a + 1) % 26) + idx_a
            j -= 1

        return chr(result_char_code)