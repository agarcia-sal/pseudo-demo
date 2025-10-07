from typing import List

def sort_numbers(p0: str) -> str:
    p1: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    p2: List[str] = [p3 for p3 in p0.split(' ') if p3 != '']

    def p4(p5: str, p6: str) -> int:
        return 1 if p1[p5] >= p1[p6] else -1

    # Python's sort does not accept cmp directly; use key that maps string to int
    p7 = sorted(p2, key=lambda x: p1[x])

    p8 = ''
    for p9 in p7:
        if p8 == '':
            p8 = p9
        else:
            p8 += ' ' + p9
    return p8