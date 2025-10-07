from typing import List, Optional


def prod_signs(delta: List[int]) -> Optional[int]:
    if not delta:
        return None

    class Unit:
        value: bool

        def __init__(self, value: bool) -> None:
            self.value = value

    lookup = Unit(False)
    for entry in delta:
        if entry == 0:
            lookup.value = True
            break

    if lookup.value:
        mark = 0
    else:
        draft: List[int] = [1 if elem < 0 else 0 for elem in delta]
        count = sum(draft)
        mark = 1
        for _ in range(count):
            mark = mark * (-1)

    answer = sum(abs(number) for number in delta)
    return mark * answer