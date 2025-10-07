from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        highest_level: int = 0
        idx: int = 0
        while idx < len(group_string):
            symbol: str = group_string[idx]
            if symbol == '(':
                depth_counter += 1
                if depth_counter > highest_level:
                    highest_level = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return highest_level

    split_groups: List[str] = []
    temp_word: str = ""
    i: int = 0
    while i <= len(parentheses_string):
        if i == len(parentheses_string) or parentheses_string[i] == ' ':
            if temp_word != "":
                split_groups.append(temp_word)
            temp_word = ""
        else:
            temp_word += parentheses_string[i]
        i += 1

    results: List[int] = []
    j: int = 0
    while j < len(split_groups):
        if split_groups[j] != "":
            results.append(parse_paren_group(split_groups[j]))
        j += 1
    return results