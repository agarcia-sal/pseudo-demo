def parse_nested_parens(paren_string):
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for character in s:
            if character == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    result_list = []
    for x in paren_string.split(' '):
        if x:
            result_list.append(parse_paren_group(x))
    return result_list