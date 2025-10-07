from typing import Generator, List


def get_max_triples(total_count: int) -> Generator[int, None, None]:
    storage_Q: List[int] = []
    index_M: int = 1
    while index_M <= total_count:
        value_L = (index_M ** 2) - index_M + 1
        storage_Q.append(value_L)
        index_M += 1

    result_Z: List[List[int]] = []
    pointer_A: int = 0
    while True:
        if pointer_A >= total_count:
            break
        pointer_B: int = pointer_A + 1
        while True:
            if pointer_B >= total_count:
                pointer_A += 1
                break
            pointer_C: int = pointer_B + 1
            while True:
                if pointer_C >= total_count:
                    pointer_B += 1
                    break
                sum_temp = storage_Q[pointer_A] + storage_Q[pointer_B] + storage_Q[pointer_C]
                if sum_temp % 3 == 0:
                    result_Z.append([storage_Q[pointer_A], storage_Q[pointer_B], storage_Q[pointer_C]])
                pointer_C += 1

    yield len(result_Z)