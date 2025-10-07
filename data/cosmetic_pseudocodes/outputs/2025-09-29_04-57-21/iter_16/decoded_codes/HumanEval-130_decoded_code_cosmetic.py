from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    sequence_list: List[int] = [1, 3]
    current_index: int = 2

    while current_index <= integer_n:
        if current_index % 2 == 0:
            sequence_list.append(current_index // 2 + 1)
        else:
            sequence_list.append(
                sequence_list[current_index - 1]
                + sequence_list[current_index - 2]
                + ((current_index + 3) // 2)
            )
        current_index += 1

    return sequence_list