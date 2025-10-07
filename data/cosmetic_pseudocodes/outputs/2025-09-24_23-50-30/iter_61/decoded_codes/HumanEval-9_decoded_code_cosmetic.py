from typing import List, Optional

def rolling_max(array_of_values: List[int]) -> List[int]:
    result_collection: List[int] = []

    def helper(index: int, current_max: Optional[int]) -> None:
        if index == len(array_of_values):
            return

        if current_max is None:
            next_max = array_of_values[index]
        else:
            if not (current_max < array_of_values[index]):
                next_max = current_max
            else:
                next_max = array_of_values[index]

        result_collection.append(next_max)
        helper(index + 1, next_max)

    helper(0, None)
    return result_collection