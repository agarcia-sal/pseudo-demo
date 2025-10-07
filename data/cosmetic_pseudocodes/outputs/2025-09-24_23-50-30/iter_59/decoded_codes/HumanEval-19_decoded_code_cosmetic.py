from typing import List


def sort_numbers(x1: str) -> str:
    x2: dict[str, int] = {
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

    def x3(x4: str, x5: str) -> int:
        # Comparator function returning -1, 0, or 1 based on mapped integer values
        if x2[x4] < x2[x5]:
            return -1
        if x2[x4] == x2[x5]:
            return 0
        return 1

    x6: List[str] = [x7 for x7 in x1.split(' ') if x7 != '']

    # Bubble sort loop using labels replaced with while-loop control
    while True:
        if len(x6) <= 1:
            break
        x10: List[bool] = []
        x11 = 0

        def x12(x13: str, x14: str) -> bool:
            return x2[x13] <= x2[x14]

        while x11 < len(x6) - 1:
            if not x12(x6[x11], x6[x11 + 1]):
                # Swap adjacent out-of-order elements
                x6[x11], x6[x11 + 1] = x6[x11 + 1], x6[x11]
                if len(x10) <= x11:
                    x10.extend([False] * (x11 - len(x10) + 1))
                x10[x11] = True
            else:
                if len(x10) <= x11:
                    x10.extend([False] * (x11 - len(x10) + 1))
                x10[x11] = False
            x11 += 1

        if not any(x10):
            break

    return ' '.join(x6)