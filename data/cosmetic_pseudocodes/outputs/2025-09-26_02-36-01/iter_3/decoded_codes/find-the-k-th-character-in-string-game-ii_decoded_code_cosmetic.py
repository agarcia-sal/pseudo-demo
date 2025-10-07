class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        size_var = 1
        operations_stack = []

        idx = 0
        while idx < len(param_operations):
            current_op = param_operations[idx]
            operations_stack.append(current_op)
            # size is doubled regardless of operation value
            size_var += size_var
            idx += 1

        result_char = 'a'
        ptr = len(operations_stack) - 1

        while ptr >= 0:
            half_size = size_var // 2  # integer division for indexing

            if param_k <= half_size:
                size_var = half_size
            else:
                param_k -= half_size
                size_var = half_size

                if operations_stack[ptr] == 1:
                    # shift character cyclically within 'a' to 'z'
                    char_code = ord(result_char)
                    offset = (char_code - ord('a') + 1) % 26
                    result_char = chr(ord('a') + offset)
            ptr -= 1

        return result_char