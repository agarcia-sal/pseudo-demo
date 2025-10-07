from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def helper(index_accumulator: int, depth_counter: int, acc_string_list: List[str], result_list: List[str]) -> List[str]:
        if index_accumulator > len(string_of_parentheses):
            return result_list
        current_char = string_of_parentheses[index_accumulator - 1]  # adjust for zero-based indexing
        if current_char == '(':
            updated_depth = depth_counter + 1
            updated_acc_string_list = acc_string_list + [current_char]
            return helper(index_accumulator + 1, updated_depth, updated_acc_string_list, result_list)
        elif current_char == ')':
            updated_depth = depth_counter - 1
            updated_acc_string_list = acc_string_list + [current_char]
            if updated_depth == 0:
                new_result_list = result_list + [''.join(updated_acc_string_list)]
                return helper(index_accumulator + 1, updated_depth, [], new_result_list)
            else:
                return helper(index_accumulator + 1, updated_depth, updated_acc_string_list, result_list)
        else:
            return helper(index_accumulator + 1, depth_counter, acc_string_list, result_list)
    return helper(1, 0, [], [])