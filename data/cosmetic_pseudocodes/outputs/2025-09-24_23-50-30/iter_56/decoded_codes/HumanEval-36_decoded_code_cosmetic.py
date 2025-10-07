from typing import List


def fizz_buzz(parameter_x: int) -> int:
    temporary_array: List[int] = []

    def recursive_loop(position_y: int) -> None:
        if position_y >= parameter_x:
            return
        if position_y % 11 == 0 or position_y % 13 == 0:
            temporary_array.append(position_y)
        recursive_loop(position_y + 1)

    recursive_loop(0)

    accumulator_string: str = ""

    def fold_string(index_v: int) -> None:
        nonlocal accumulator_string
        if index_v >= len(temporary_array):
            return
        accumulator_string += str(temporary_array[index_v])
        fold_string(index_v + 1)

    fold_string(0)

    count_seven_chars: int = 0

    def count_seven_character(index_w: int, accumulator_count: int) -> None:
        nonlocal count_seven_chars
        if index_w >= len(accumulator_string):
            count_seven_chars = accumulator_count
            return
        count_seven_character(index_w + 1, accumulator_count + (1 if accumulator_string[index_w] == '7' else 0))

    count_seven_character(0, 0)
    return count_seven_chars