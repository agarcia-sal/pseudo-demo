from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result: List[str] = [""]
    current_string: List[str] = [""]
    current_depth: int = 0

    for index in range(len(paren_string)):
        c = paren_string[index]
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                joined_string = ""
                for join_index in range(len(current_string)):
                    joined_string += current_string[join_index]
                result.append(joined_string)
                current_string.clear()

    return result