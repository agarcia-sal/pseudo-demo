from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    result_list = []
    split_list = []
    current_word = ''
    for current_char in paren_string:
        if current_char == ' ':
            if current_word != '':
                split_list.append(current_word)
                current_word = ''
        else:
            current_word += current_char
    if current_word != '':
        split_list.append(current_word)

    for element in split_list:
        result_list.append(parse_paren_group(element))

    return result_list