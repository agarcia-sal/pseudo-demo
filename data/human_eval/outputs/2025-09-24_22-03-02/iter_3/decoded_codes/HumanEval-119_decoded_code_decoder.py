def match_parens(lst):
    def check(s):
        val = 0
        for c in s:
            val += 1 if c == '(' else -1
            if val < 0:
                return False
        return val == 0

    return 'Yes' if check(lst[0] + lst[1]) or check(lst[1] + lst[0]) else 'No'