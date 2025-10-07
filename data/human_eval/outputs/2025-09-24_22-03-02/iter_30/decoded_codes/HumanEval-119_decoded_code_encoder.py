def match_parens(lst) -> str:
    def check(s: str) -> bool:
        val = 0
        for char in s:
            if char == '(':
                val += 1
            else:
                val -= 1
            if val < 0:
                return False
        return val == 0

    s1 = lst[0] + lst[1]
    s2 = lst[1] + lst[0]

    return 'Yes' if check(s1) or check(s2) else 'No'