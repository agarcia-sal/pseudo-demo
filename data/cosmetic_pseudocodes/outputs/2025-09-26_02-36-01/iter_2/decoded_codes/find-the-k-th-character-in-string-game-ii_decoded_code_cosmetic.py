class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        current_length = 1
        operations_list = []

        index = 0
        while index < len(param_operations):
            operation_element = param_operations[index]
            operations_list.append(operation_element)
            # According to pseudocode logic, current_length doubles regardless of operation_element
            current_length += current_length
            index += 1

        result_char = 'a'
        pos = len(operations_list) - 1
        while pos >= 0:
            half_length = current_length // 2
            if param_k <= half_length:
                current_length = half_length
            else:
                param_k -= half_length
                current_length = half_length
                if operations_list[pos] == 1:
                    # Shift character by 1 in cyclic manner from 'a' to 'z'
                    new_code = ((ord(result_char) - ord('a') + 1) % 26) + ord('a')
                    result_char = chr(new_code)
            pos -= 1

        return result_char