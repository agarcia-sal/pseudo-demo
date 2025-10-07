from typing import List


def words_string(input_string: str) -> List[str]:
    def transform_chars(index: int, acc: str) -> str:
        if index >= len(input_string):
            return acc
        current_char = input_string[index]
        new_acc = acc + (' ' if current_char == ',' else current_char)
        return transform_chars(index + 1, new_acc)

    if len(input_string) == 0:
        return []
    modified_str = transform_chars(0, "")
    return modified_str.split()