from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    def inner_collect(i: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if i >= len(matrix):
            return acc
        else:
            def inner_col(j: int, row_acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
                if j >= len(matrix[i]):
                    return row_acc
                else:
                    updated_acc = row_acc + [(i, j)] if matrix[i][j] == key else row_acc
                    return inner_col(j + 1, updated_acc)
            new_acc = inner_col(0, acc)
            return inner_collect(i + 1, new_acc)

    collected = inner_collect(0, [])

    def sort_by_first_then_second(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        def insert_firstwise(el: Tuple[int, int], sorted_lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if not sorted_lst:
                return [el]
            else:
                h = sorted_lst[0]
                t = sorted_lst[1:]
                if el[0] < h[0]:
                    return [el] + sorted_lst
                elif el[0] == h[0] and el[1] > h[1]:
                    return [el] + sorted_lst
                else:
                    return [h] + insert_firstwise(el, t)

        res: List[Tuple[int, int]] = []
        for item in lst:
            res = insert_firstwise(item, res)
        return res

    return sort_by_first_then_second(collected)