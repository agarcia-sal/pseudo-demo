from typing import List, Optional

def rolling_max(collection_of_values: List[int]) -> List[int]:
    accumulator_max: Optional[int] = None
    outcome_collection: List[int] = []

    def process_item(index: int) -> None:
        if index >= len(collection_of_values):
            return

        if accumulator_max is None:
            nonlocal accumulator_max
            accumulator_max = collection_of_values[index]
        else:
            nonlocal accumulator_max
            if accumulator_max < collection_of_values[index]:
                accumulator_max = collection_of_values[index]

        outcome_collection.append(accumulator_max)
        process_item(index + 1)

    process_item(0)
    return outcome_collection