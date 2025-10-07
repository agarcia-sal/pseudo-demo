from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    list_of_chars: List[str] = list(str(integer_x))
    count_chars: int = len(list_of_chars)

    if not (integer_shift <= count_chars):
        # Reverse list_of_chars by iterating indices from count_chars -1 down to 0
        result_chars: List[str] = []
        for index in range(count_chars - 1, -1, -1):
            result_chars.append(list_of_chars[index])
        return ''.join(result_chars)

    split_point: int = count_chars - integer_shift

    part_one: str = ''
    part_two: str = ''

    # Indices in pseudocode are 1-based, adjust by subtracting 1 for 0-based indexing
    for i in range(1, split_point + 1):
        part_two += list_of_chars[i - 1]

    for j in range(split_point + 1, count_chars + 1):
        part_one += list_of_chars[j - 1]

    return part_one + part_two