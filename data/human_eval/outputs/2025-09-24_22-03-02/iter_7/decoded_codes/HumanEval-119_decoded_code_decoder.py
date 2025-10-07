def match_parens(lst):
    def check(s):
        val = 0
        for character in s:
            if character == '(':
                val += 1
            else:
                val -= 1
            if val < 0:
                return False
        return val == 0

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]

    if check(S1) or check(S2):
        return 'Yes'
    else:
        return 'No'