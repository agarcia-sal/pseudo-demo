from typing import List


def string_sequence(integer_n: int) -> str:
    def build_sequence(current: int, limit: int) -> List[str]:
        if current > limit:
            return []
        return [str(current)] + build_sequence(current + 1, limit)

    result_list = build_sequence(0, integer_n)
    accumulator = ""
    for element in result_list:
        accumulator += ("" if accumulator == "" else " ") + element
    return accumulator