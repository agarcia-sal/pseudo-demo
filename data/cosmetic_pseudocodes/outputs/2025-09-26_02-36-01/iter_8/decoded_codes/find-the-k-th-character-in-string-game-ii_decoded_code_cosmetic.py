class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        alpha_char = 'a'
        ops_sequence = []
        current_length = 1  # (2 - 1) = 1

        def appendOp(op_val: int):
            ops_sequence.append(op_val)

        index_op = 0
        while index_op < len(param_operations):
            appendOp(param_operations[index_op])
            # Both branches effectively multiply current_length by 2
            if param_operations[index_op] == 0:
                current_length *= 2
            else:
                current_length *= 2
            index_op += 1

        idx = len(ops_sequence) - 1  # LENGTH(ops_sequence) - (2 - 1) = len-1

        while idx >= 0:
            half_length = current_length // 2
            if param_k <= half_length:
                current_length = half_length
            else:
                param_k -= half_length
                current_length = half_length
                if ops_sequence[idx] == 1:
                    char_code = ord(alpha_char)
                    char_code += 1
                    if char_code > ord('z'):
                        char_code = ord('a')
                    alpha_char = chr(char_code)
            idx -= 1

        return alpha_char