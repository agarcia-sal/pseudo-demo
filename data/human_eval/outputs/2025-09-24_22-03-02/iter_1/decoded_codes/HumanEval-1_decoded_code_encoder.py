def separate_paren_groups(s):
    res, cur, depth = [], [], 0
    for c in s:
        if c == '(':
            depth += 1
            cur.append(c)
        elif c == ')':
            depth -= 1
            cur.append(c)
            if depth == 0:
                res.append(''.join(cur))
                cur.clear()
    return res