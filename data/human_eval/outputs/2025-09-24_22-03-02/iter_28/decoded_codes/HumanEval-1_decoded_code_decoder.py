from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = [""]
    current_string = []
    current_depth = 0
    for index in range(len(paren_string)):
        c = paren_string[index]
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)
            if current_depth == 0:
                temp_string = ""
                for index2 in range(len(current_string)):
                    temp_string += current_string[index2]
                result.append(temp_string)
                current_string = []
    return result