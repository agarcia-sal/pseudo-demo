from typing import Tuple

def reverse_delete(string_input: str, string_remove: str) -> Tuple[str, str]:
    def helper_filter(index_accum: int, filtered_accum: str) -> str:
        if index_accum >= len(string_input):
            return filtered_accum
        if string_input[index_accum] in string_remove:
            return helper_filter(index_accum + 1, filtered_accum)
        else:
            return helper_filter(index_accum + 1, filtered_accum + string_input[index_accum])

    result_string = helper_filter(0, "")
    reversed_string = ""

    def reverse_iterate(position: int) -> None:
        nonlocal reversed_string
        if position < 0:
            return
        reversed_string += result_string[position]
        reverse_iterate(position - 1)

    reverse_iterate(len(result_string) - 1)
    return result_string, reversed_string