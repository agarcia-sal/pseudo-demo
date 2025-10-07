from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        accMax: int = 0
        accCur: int = 0

        def recIter(h: str, accMax: int, accCur: int) -> int:
            if not h:
                return accMax
            c, t = h[0], h[1:]
            if c == '(':
                newCur = accCur + 1
                newMax = newCur if newCur > accMax else accMax
                return recIter(t, newMax, newCur)
            elif c == ')':
                return recIter(t, accMax, accCur - 1)
            else:
                return recIter(t, accMax, accCur)

        result = recIter(group_string, accMax, accCur)
        return result

    groups = [group for group in parentheses_string.split(' ') if group != '']
    results = [parse_paren_group(g) for g in groups]
    return results