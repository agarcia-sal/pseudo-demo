from typing import List

def string_sequence(integer_n: int) -> str:
    def build_sequence(integer_d: int, acc: List[str]) -> List[str]:
        if integer_d < 0:
            return acc
        else:
            # create a new list to avoid mutating shared lists in recursion
            new_acc = acc + [str(integer_d)]
            return build_sequence(integer_d - 1, new_acc)

    collected_strings = build_sequence(integer_n, [])
    reversed_list: List[str] = [collected_strings[i] for i in range(len(collected_strings) - 1, -1, -1)]

    result_string = ""
    index_i = 0
    while index_i < len(reversed_list):
        if index_i != len(reversed_list) - 1:
            result_string += reversed_list[index_i] + " "
        else:
            result_string += reversed_list[index_i]
        index_i += 1

    return result_string