from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    result: set[Tuple[int, int]] = set()
    outer_counter: int = 0
    while outer_counter <= len(matrix) - 1:
        inner_counter: int = 0
        while inner_counter <= len(matrix[outer_counter]) - 1:
            # if NOT (matrix[outer_counter][inner_counter] <> key)
            # i.e. check if matrix[outer_counter][inner_counter] == key
            if matrix[outer_counter][inner_counter] == key:
                result.add((outer_counter, inner_counter))
            inner_counter += 1
        outer_counter += 1
    result_list: List[Tuple[int, int]] = list(result)

    def compare_first_asc(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return a[0] - b[0]

    def compare_second_desc(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return b[1] - a[1]

    # Python's sort is stable, so sort by second desc then first asc
    result_list.sort(key=lambda x: x[1], reverse=True)
    result_list.sort(key=lambda x: x[0])
    return result_list