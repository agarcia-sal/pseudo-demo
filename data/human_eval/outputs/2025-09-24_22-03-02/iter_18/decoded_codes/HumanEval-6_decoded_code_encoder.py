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

    result: List[int] = []
    words: List[str] = []
    current_word = ''
    for char in paren_string:
        if char == ' ':
            if current_word != '':
                words.append(current_word)
                current_word = ''
        else:
            current_word += char
    if current_word != '':
        words.append(current_word)

    for word in words:
        depth_value = parse_paren_group(word)
        result.append(depth_value)
    return result