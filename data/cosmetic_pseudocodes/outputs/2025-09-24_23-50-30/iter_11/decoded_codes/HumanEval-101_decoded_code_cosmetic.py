from typing import List


def words_string(input_string: str) -> List[str]:
    result_list: List[str] = []

    for index in range(1, len(input_string) + 1):
        element: str = input_string[index - 1]
        if element != ',':
            result_list.append(element)
        else:
            result_list.append(' ')

    combined: str = "".join(result_list)

    return combined.split(" ")