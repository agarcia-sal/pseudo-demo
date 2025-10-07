from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    u: dict[int, int] = {}

    def v(w: List[int]) -> None:
        if not w:
            return
        x = w[0]
        u[x] = u.get(x, 0) + 1
        v(w[1:])

    v(list_of_numbers)

    for y in u:
        if u[y] > 2:
            return False

    z = 1
    while z < len(list_of_numbers):
        if not (list_of_numbers[z - 1] <= list_of_numbers[z]):
            return False
        z += 1

    return True