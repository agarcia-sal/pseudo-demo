from typing import Sequence, Optional, Union


def prod_signs(collection_of_numbers: Sequence[Union[int, float]]) -> Optional[Union[int, float]]:
    if not collection_of_numbers:
        return None

    if 0 in collection_of_numbers:
        result_indicator: int = 0
    else:
        negative_count: int = 0
        for value in collection_of_numbers:
            if value < 0:
                negative_count += 1
        # result_indicator is (-1) ** negative_count
        result_indicator = 1
        temp_count = negative_count
        while temp_count > 0:
            result_indicator *= -1
            temp_count -= 1

    aggregate_magnitude: Union[int, float] = 0
    for value in collection_of_numbers:
        aggregate_magnitude += abs(value)

    return result_indicator * aggregate_magnitude