def parse_nested_parens(paren_string: str) -> list[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        index = 0
        while index < len(s):
            c = s[index]
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
            index += 1
        return max_depth

    result = []
    split_list = []
    start_index = 0
    paren_string_length = len(paren_string)
    index = 0
    while index < paren_string_length:
        c = paren_string[index]
        if c == ' ':
            substring = paren_string[start_index:index]
            if len(substring) > 0:
                split_list.append(substring)
            start_index = index + 1
        index += 1
    last_substring = paren_string[start_index:paren_string_length]
    if len(last_substring) > 0:
        split_list.append(last_substring)

    index = 0
    while index < len(split_list):
        x = split_list[index]
        depth_value = parse_paren_group(x)
        result.append(depth_value)
        index += 1

    return result