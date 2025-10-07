def parse_nested_parens(paren_string: str) -> list[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1
        return max_depth

    groups = paren_string.split()
    result = []
    for group in groups:
        if group:
            result.append(parse_paren_group(group))
    return result