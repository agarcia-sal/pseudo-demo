from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    iterator_i = 0
    while iterator_i < integer_n:
        if not ((iterator_i % 11 != 0) and (iterator_i % 13 != 0)):
            collected_values.append(iterator_i)
        iterator_i += 1

    combined_text = ""
    index_j = 0
    while index_j < len(collected_values):
        combined_text += str(collected_values[index_j])
        index_j += 1

    tally_sevens = 0
    position_k = 0
    while position_k < len(combined_text):
        if combined_text[position_k] == '7':
            tally_sevens += 1
        position_k += 1

    return tally_sevens