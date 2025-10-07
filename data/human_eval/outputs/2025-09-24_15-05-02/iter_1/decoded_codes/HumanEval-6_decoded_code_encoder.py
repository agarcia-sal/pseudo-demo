def parse_nested_parens(s):
    def parse_grp(g):
        max_depth = 0
        depth = 0
        for c in g:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif c == ')':
                depth -= 1
        return max_depth
    return [parse_grp(x) for x in s.split(' ') if x]