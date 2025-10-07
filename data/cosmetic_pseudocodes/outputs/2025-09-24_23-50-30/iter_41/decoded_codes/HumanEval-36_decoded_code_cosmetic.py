from typing import List


def fizz_buzz(subject_p: int) -> int:
    accumulator_1: List[int] = []

    def function_loop(index_x: int) -> None:
        if not (index_x < subject_p):
            return
        if index_x % 11 == 0:
            accumulator_1.append(index_x)
        elif index_x % 13 == 0:
            accumulator_1.append(index_x)
        function_loop(index_x + 1)

    function_loop(0)

    accumulator_2: str = ""

    def function_concat(lst_y: List[int], idx_z: int) -> None:
        nonlocal accumulator_2
        if idx_z >= len(lst_y):
            return
        accumulator_2 += str(lst_y[idx_z])
        function_concat(lst_y, idx_z + 1)

    function_concat(accumulator_1, 0)

    counter_a: int = 0

    def function_count(string_b: str, idx_c: int) -> None:
        nonlocal counter_a
        if idx_c >= len(string_b):
            return
        counter_a += 1 if string_b[idx_c] == '7' else 0
        function_count(string_b, idx_c + 1)

    function_count(accumulator_2, 0)

    return counter_a