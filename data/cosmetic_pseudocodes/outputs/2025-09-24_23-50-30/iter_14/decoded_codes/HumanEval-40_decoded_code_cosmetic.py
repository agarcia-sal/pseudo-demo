from typing import List


def triples_sum_to_zero(array_numbers: List[int]) -> bool:
    limit = len(array_numbers) - 2
    for x in range(limit + 1):
        for y in range(x + 1, limit + 2):
            for z in range(y + 1, len(array_numbers)):
                if array_numbers[z] + array_numbers[y] + array_numbers[x] == 0:
                    return True
    return False