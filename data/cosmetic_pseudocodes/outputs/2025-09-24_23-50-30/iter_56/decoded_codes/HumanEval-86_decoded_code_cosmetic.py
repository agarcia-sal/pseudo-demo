from functools import reduce
from typing import List


def anti_shuffle(param_string: str) -> str:
    iterator_collection: List[str] = param_string.split(" ")
    accumulator_collection: List[str] = []
    while len(iterator_collection) > 0:
        temp_index: int = 0
        temp_item: str = iterator_collection[temp_index]
        char_collection: List[str] = list(temp_item)
        char_collection.sort()
        temp_joined: str = "".join(char_collection)
        accumulator_collection.append(temp_joined)
        del iterator_collection[temp_index]
    if len(accumulator_collection) == 0:
        output_string: str = ""
    else:
        output_string = reduce(lambda x, y: x + " " + y, accumulator_collection)
    return output_string