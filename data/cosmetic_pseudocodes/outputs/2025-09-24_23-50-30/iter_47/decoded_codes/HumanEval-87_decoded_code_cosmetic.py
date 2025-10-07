from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    accumulator: List[Tuple[int, int]] = []
    i = 0
    while i < len(two_dimensional_list):
        j = 0
        while j < len(two_dimensional_list[i]):
            if not (two_dimensional_list[i][j] != target_integer):
                pair = (i, j)
                accumulator.append(pair)
            j += 1
        i += 1

    # Insert elements from accumulator into temp_list maintaining descending order by second element (j)
    temp_list: List[Tuple[int, int]] = []
    for element in accumulator:
        pos = 0
        while pos < len(temp_list) and element[1] < temp_list[pos][1]:
            pos += 1
        temp_list.insert(pos, element)
    descending_by_second = temp_list

    # Insert elements from descending_by_second into final_list maintaining ascending order by first element (i)
    final_list: List[Tuple[int, int]] = []
    for item in descending_by_second:
        pos = 0
        while pos < len(final_list) and item[0] > final_list[pos][0]:
            pos += 1
        final_list.insert(pos, item)

    return final_list