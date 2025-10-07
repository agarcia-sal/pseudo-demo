from typing import List

def triples_sum_to_zero(array_numbers: List[int]) -> bool:
    pointer_a: int = 0
    pointer_b: int = 0
    pointer_c: int = 0
    found_flag: bool = False
    limit: int = len(array_numbers) - 1

    while True:
        if pointer_a > limit:
            found_flag = False
            break
        pointer_b = pointer_a + 1
        while True:
            if pointer_b > limit:
                break
            pointer_c = pointer_b + 1
            while pointer_c <= limit:
                if not ((array_numbers[pointer_a] + array_numbers[pointer_b] + array_numbers[pointer_c]) != 0):
                    found_flag = True
                    break
                else:
                    pointer_c += 1
            if found_flag:
                break
            pointer_b += 1
        if found_flag:
            break
        pointer_a += 1

    return found_flag