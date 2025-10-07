from typing import List

def words_string(input_string: str) -> List[str]:
    def transform(index: int, acc: str) -> str:
        if index >= len(input_string):
            return acc
        current_char = input_string[index]
        updated_acc = acc + (' ' if current_char == ',' else current_char)
        return transform(index + 1, updated_acc)

    if len(input_string) == 0:
        return []

    replaced_string = transform(0, "")
    word_array = replaced_string.split()
    return word_array