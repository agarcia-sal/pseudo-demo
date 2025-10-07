from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = ['']
    current_string = ['']
    current_depth = 0
    index = 0
    while index < len(paren_string):
        c = paren_string[index]
        if c == '(':
            current_depth += 1
            current_string.append('(')
        elif c == ')':
            current_depth -= 1
            current_string.append(')')
            if current_depth == 0:
                joined_string = ''
                join_index = 0
                while join_index < len(current_string):
                    joined_string += current_string[join_index]
                    join_index += 1
                result.append(joined_string)
                current_string = ['']
        index += 1
    return result