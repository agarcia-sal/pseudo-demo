from typing import List

def make_a_pile(input_num: int) -> List[int]:
    result_collection: List[int] = []
    iterator: int = 0

    while iterator < input_num:
        result_collection.append(input_num + (iterator * 2))
        iterator += 1

    return result_collection