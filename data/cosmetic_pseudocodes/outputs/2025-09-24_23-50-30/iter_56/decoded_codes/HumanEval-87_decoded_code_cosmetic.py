from typing import List, Tuple


def get_row(p_matrix: List[List[int]], p_value: int) -> List[Tuple[int, int]]:
    def traverse_rows(i_r: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if i_r < len(p_matrix):
            def traverse_cols(i_c: int, acc2: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
                if i_c < len(p_matrix[i_r]):
                    if p_matrix[i_r][i_c] == p_value:
                        acc2 = acc2 + [(i_r, i_c)]
                    return traverse_cols(i_c + 1, acc2)
                else:
                    return acc2

            return traverse_rows(i_r + 1, traverse_cols(0, acc))
        else:
            return acc

    coords = traverse_rows(0, [])

    def compare_by_first_then_second(t1: Tuple[int, int], t2: Tuple[int, int]) -> int:
        if t1[0] < t2[0]:
            return -1
        elif t1[0] > t2[0]:
            return 1
        elif t1[1] > t2[1]:
            return -1
        elif t1[1] < t2[1]:
            return 1
        else:
            return 0

    coords.sort(key=lambda t: (t[0], -t[1]))

    return coords