from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def helper_length_agg(paramList_snake_case: List[str], accumulator_camPle: int) -> int:
        if not paramList_snake_case:
            return accumulator_camPle
        head_camel, *tail_camel = paramList_snake_case
        new_accum = accumulator_camPle + len(head_camel)
        return helper_length_agg(tail_camel, new_accum)

    LenOneCamelCase = helper_length_agg(list_one, 0)
    LenTwo_snake_case = helper_length_agg(list_two, 0)

    if not (LenOneCamelCase > LenTwo_snake_case):
        return list_one
    else:
        return list_two