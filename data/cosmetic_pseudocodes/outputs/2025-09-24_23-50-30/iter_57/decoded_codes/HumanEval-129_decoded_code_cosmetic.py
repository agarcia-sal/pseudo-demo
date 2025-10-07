from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size_be_forever: int = len(grid)
    sentinel_val: int = (size_be_forever * size_be_forever) + 1

    idx_x: int = 0
    while idx_x < size_be_forever:
        idx_y: int = 0
        while idx_y < size_be_forever:
            if grid[idx_x][idx_y] != 0:
                if grid[idx_x][idx_y] == 1:
                    candidates_accumulator: List[int] = []
                    if idx_x != 0:
                        candidates_accumulator.append(grid[idx_x - 1][idx_y])
                    if idx_y != 0:
                        candidates_accumulator.append(grid[idx_x][idx_y - 1])
                    if idx_x != size_be_forever - 1:
                        candidates_accumulator.append(grid[idx_x + 1][idx_y])
                    if idx_y != size_be_forever - 1:
                        candidates_accumulator.append(grid[idx_x][idx_y + 1])

                    minimum_candidate: int = sentinel_val
                    iterator_c: int = 0
                    while iterator_c < len(candidates_accumulator):
                        if candidates_accumulator[iterator_c] < minimum_candidate:
                            minimum_candidate = candidates_accumulator[iterator_c]
                        iterator_c += 1

                    sentinel_val = minimum_candidate
            idx_y += 1
        idx_x += 1

    final_sequence: List[int] = []
    counter_was: int = 0
    while counter_was < k:
        result_element: int = 1 if (counter_was % 2 == 0) else sentinel_val
        final_sequence.append(result_element)
        counter_was += 1

    return final_sequence