from typing import List


def words_string(input_string: str) -> List[str]:
    def helper_function(curr_index: int, acc_list: List[str]) -> List[str]:
        if curr_index >= len(input_string):
            combined_string = ''.join(acc_list)
            return combined_string.split()
        else:
            current_char = input_string[curr_index]
            if current_char == ',':
                updated_list = acc_list + [' ']
            else:
                updated_list = acc_list + [current_char]
            return helper_function(curr_index + 1, updated_list)

    return [] if len(input_string) == 0 else helper_function(0, [])