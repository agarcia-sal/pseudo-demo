from typing import List


def words_string(input_string: str) -> List[str]:
    def recurse_replace_comma(index: int, acc: str) -> str:
        if index >= len(input_string):
            return acc
        cur_char = input_string[index]
        updated_acc = acc + (cur_char if cur_char != ',' else ' ')
        return recurse_replace_comma(index + 1, updated_acc)

    if len(input_string) == 0:
        return []

    replaced_str = recurse_replace_comma(0, "")
    word_array = replaced_str.split(" ")
    return word_array