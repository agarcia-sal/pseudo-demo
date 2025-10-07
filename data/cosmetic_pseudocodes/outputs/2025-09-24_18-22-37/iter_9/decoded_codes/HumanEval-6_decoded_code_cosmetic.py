from typing import List

def parse_nested_parens(string_input: str) -> List[int]:
    def parse_paren_group(inner_string: str) -> int:
        depth_counter: int = 0
        max_depth_value: int = 0
        for current_char in inner_string:
            if current_char == '(':
                depth_counter += 1
                if depth_counter > max_depth_value:
                    max_depth_value = depth_counter
            elif current_char == ')':
                depth_counter -= 1
        return max_depth_value

    split_groups = string_input.split(' ')
    result_list: List[int] = []
    for elem in split_groups:
        if elem != '':
            temp_result = parse_paren_group(elem)
            result_list.append(temp_result)
    return result_list