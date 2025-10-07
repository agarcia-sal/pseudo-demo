from typing import List


def anti_shuffle(str_param: str) -> str:
    words_collection: List[str] = [
        "".join(sorted(list(elem_param))) for elem_param in str_param.split(" ")
    ]
    result_accumulator: str = ""
    index_position: int = 0
    while index_position < len(words_collection):
        result_accumulator += words_collection[index_position]
        if index_position != (len(words_collection) - 1):
            result_accumulator += " "
        index_position += 1
    return result_accumulator