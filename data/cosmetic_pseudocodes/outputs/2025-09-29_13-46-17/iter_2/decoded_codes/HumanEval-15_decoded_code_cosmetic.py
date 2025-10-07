from typing import List


def string_sequence(integer_n: int) -> str:
    string_list: List[str] = []

    def convert_and_append(index: int) -> None:
        if index > integer_n:
            return
        string_list.append(str(index))
        convert_and_append(index + 1)

    convert_and_append(0)
    return " ".join(string_list)