def check(s):
    val = 0
    for c in s:
        val += 1 if c == '(' else -1
        if val < 0:
            return False
    return val == 0

def match_parens(lst):
    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'