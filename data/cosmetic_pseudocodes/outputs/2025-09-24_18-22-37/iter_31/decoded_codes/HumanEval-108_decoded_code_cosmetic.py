from typing import Iterable, List, Union

def count_nums(input_collection: Iterable[Union[int, float]]) -> int:
    def digits_sum(input_number: Union[int, float]) -> int:
        factor: int = 1
        if not (input_number >= 0):
            input_number = -input_number
            factor = -1

        chars: List[str] = list(str(input_number))
        digits: List[int] = [int(c) for c in chars]

        digits[0] *= factor

        total: int = sum(digits)
        return total

    sums_collection: List[int] = []
    index: int = 0
    input_list = list(input_collection)
    while index < len(input_list):
        current_element = input_list[index]
        sums_collection.append(digits_sum(current_element))
        index += 1

    count_positive: int = 0
    for each_sum in sums_collection:
        if each_sum > 0:
            count_positive += 1

    return count_positive