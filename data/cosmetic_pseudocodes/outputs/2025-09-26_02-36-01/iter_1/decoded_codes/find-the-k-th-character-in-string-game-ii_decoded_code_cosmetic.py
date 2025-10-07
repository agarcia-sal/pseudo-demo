class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        current_length = 1
        operation_list = []

        for operation_element in param_operations:
            operation_list.append(operation_element)
            current_length *= 2

        result_char = 'a'

        for index in range(len(operation_list) - 1, -1, -1):
            half_length = current_length // 2
            if param_k > half_length:
                param_k -= half_length
                if operation_list[index] == 1:
                    result_char = 'a' if result_char == 'z' else chr(ord(result_char) + 1)
            current_length = half_length

        return result_char