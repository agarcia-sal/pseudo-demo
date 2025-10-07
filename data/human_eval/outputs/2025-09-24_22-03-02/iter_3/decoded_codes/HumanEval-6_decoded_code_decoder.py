def parse_nested_parens(paren_string: str) -> list[int]:
    def parse_paren_group(s: str) -> int:
        depth = max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    return [parse_paren_group(x) for x in paren_string.split() if x]