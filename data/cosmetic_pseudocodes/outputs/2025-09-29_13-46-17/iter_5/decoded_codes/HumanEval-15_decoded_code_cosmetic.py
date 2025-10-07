from typing import List


def string_sequence(integer_n: int) -> str:
    def helper(current_index: int, limit: int, accumulator: List[str]) -> List[str]:
        if current_index > limit:
            return accumulator
        updated_accumulator = accumulator + [str(current_index)]
        return helper(current_index + 1, limit, updated_accumulator)

    string_list = helper(0, integer_n, [])
    result = ""
    for element in string_list:
        if len(result) == 0:
            result = element
        else:
            result += " " + element
    return result