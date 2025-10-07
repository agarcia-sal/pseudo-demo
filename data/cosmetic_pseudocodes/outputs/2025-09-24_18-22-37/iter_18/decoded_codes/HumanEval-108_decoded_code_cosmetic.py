from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(y: int) -> int:
        a = 1
        if y < 0:
            y = -y
            a = -1

        s = str(y)
        b: List[int] = [int(ch) for ch in s]
        b[0] = b[0] * a

        total = 0
        idx = 0
        while idx < len(b):
            total += b[idx]
            idx += 1
        return total

    c: List[int] = []
    idx_outer = 0
    while idx_outer < len(array_of_integers):
        current_element = array_of_integers[idx_outer]
        x = digits_sum(current_element)
        c.append(x)
        idx_outer += 1

    result_list: List[int] = [val for val in c if val > 0]

    return len(result_list)