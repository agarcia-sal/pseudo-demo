from typing import List


def parse_nested_parens(str_of_parens: str) -> List[int]:
    def parse_paren_group(subgroup: str) -> int:
        depth_current = 0
        depth_max = 0
        idx = 0
        while idx < len(subgroup):
            char = subgroup[idx]
            if char == '(':
                depth_current += 1
                if depth_current > depth_max:
                    depth_max = depth_current
            else:
                depth_current -= 1
            idx += 1
        return depth_max

    segments: List[str] = []
    word = ""
    for char in str_of_parens:
        if char == ' ':
            if word != "":
                segments.append(word)
                word = ""
        else:
            word += char
    if word != "":
        segments.append(word)

    results: List[int] = [parse_paren_group(element) for element in segments]
    return results