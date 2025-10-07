from typing import Sequence, Union

def sum_squares(collection_of_numbers: Sequence[Union[int, float]]) -> Union[int, float]:
    def helper(counter: int, accumulator: Union[int, float]) -> Union[int, float]:
        if counter < 0:
            return accumulator
        if (counter % 3) == 0:
            # counter divisible by 3
            return helper(counter - 1, accumulator + collection_of_numbers[counter] ** 2)
        if (counter % 4) == 0 and (counter % 3) != 0:
            # divisible by 4 but not by 3
            return helper(counter - 1, accumulator + collection_of_numbers[counter] ** 3)
        # all other cases
        return helper(counter - 1, accumulator + collection_of_numbers[counter])

    return helper(len(collection_of_numbers) - 1, 0)