def is_nested(s):
    O = [i for i, ch in enumerate(s) if ch == '[']
    C = [i for i, ch in enumerate(s) if ch == ']'][::-1]
    cnt, i = 0, 0
    for idx in O:
        if i < len(C) and idx < C[i]:
            cnt += 1
            i += 1
    return cnt >= 2