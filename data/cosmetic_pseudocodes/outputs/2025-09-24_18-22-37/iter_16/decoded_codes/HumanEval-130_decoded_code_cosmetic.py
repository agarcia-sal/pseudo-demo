from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]
    pqr: List[int] = [1, 3]
    counter: int = 2
    while counter <= integer_n:
        is_even: bool = (counter % 2) == 0
        if is_even:
            new_element: int = (counter // 2) + 1
            pqr.append(new_element)
        else:
            left_idx: int = counter - 1
            right_idx: int = counter - 2
            val1: int = pqr[left_idx]
            val2: int = pqr[right_idx]
            add_val: int = (counter + 3) // 2
            combined: int = val1 + val2 + add_val
            pqr.append(combined)
        counter += 1
    return pqr