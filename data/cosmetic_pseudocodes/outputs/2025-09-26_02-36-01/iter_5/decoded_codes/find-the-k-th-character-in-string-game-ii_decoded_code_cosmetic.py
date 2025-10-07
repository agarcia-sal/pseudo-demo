class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        def helper_decrement(index_current: int, length_current: int, position_current: int, current_char: str, ops_collection: list[int]) -> str:
            if index_current < 0:
                return current_char

            half_length = length_current // 2

            if position_current <= half_length:
                return helper_decrement(index_current - 1, half_length, position_current, current_char, ops_collection)
            else:
                updated_position = position_current - half_length
                updated_char = current_char
                if ops_collection[index_current] == 1:
                    char_code = ord(updated_char)
                    if char_code == ord('z'):
                        updated_char = 'a'
                    else:
                        updated_char = chr(char_code + 1)
                return helper_decrement(index_current - 1, half_length, updated_position, updated_char, ops_collection)

        length_calc = 1
        ops_list = []

        index = 0
        while index < len(operations):
            op_curr = operations[index]
            ops_list.append(op_curr)
            multiplier = 2 * 1
            length_calc = length_calc * multiplier // 2
            index += 1

        initial_character = 'a'
        ops_last_index = len(ops_list) - 1
        result_char = helper_decrement(ops_last_index, length_calc, k, initial_character, ops_list)

        return result_char