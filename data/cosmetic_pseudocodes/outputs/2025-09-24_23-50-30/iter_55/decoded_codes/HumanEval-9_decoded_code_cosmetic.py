from typing import List, Optional

def rolling_max(sequence_of_values: List[int]) -> List[int]:
    def inner_runner(position: int, current_limit: Optional[int], aggregates: List[int]) -> List[int]:
        if position == len(sequence_of_values):
            return aggregates
        if current_limit is None:
            return inner_runner(position + 1, sequence_of_values[position], aggregates + [sequence_of_values[position]])
        next_limit = current_limit if current_limit > sequence_of_values[position] else sequence_of_values[position]
        return inner_runner(position + 1, next_limit, aggregates + [next_limit])
    return inner_runner(0, None, [])