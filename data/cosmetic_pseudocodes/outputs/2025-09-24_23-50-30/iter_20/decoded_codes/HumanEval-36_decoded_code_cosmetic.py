from typing import Set


def fizz_buzz(integer_n: int) -> int:
    accumulated_set: Set[int] = set()

    def collect(dividend: int, limit: int, container: Set[int]) -> Set[int]:
        index = 0
        while index < limit:
            if index % dividend == 0:
                container = container.union({index})
            index += 1
        return container

    accumulated_set = collect(11, integer_n, accumulated_set)
    accumulated_set = collect(13, integer_n, accumulated_set)

    assembled_string = ""
    for element in accumulated_set:
        assembled_string += str(element)

    def count_characters(target_string: str, target_char: str) -> int:
        accumulator = 0
        pointer = 0
        while pointer < len(target_string):
            if target_string[pointer] == target_char:
                accumulator += 1
            pointer += 1
        return accumulator

    return count_characters(assembled_string, "7")