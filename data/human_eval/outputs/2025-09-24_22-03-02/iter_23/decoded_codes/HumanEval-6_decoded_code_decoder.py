from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    result: List[int] = []
    parts: List[str] = []
    current_word = ""
    for i in range(len(paren_string)):
        char = paren_string[i]
        if char == ' ':
            if current_word != "":
                parts.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word != "":
        parts.append(current_word)

    for i in range(len(parts)):
        x = parts[i]
        result.append(parse_paren_group(x))

    return result