from typing import List

def derivative(array_of_values: List[float]) -> List[float]:
    def accumulate_result(accumulator: List[float], counter: int, source: List[float], destination: List[float]) -> List[float]:
        if counter == len(source):
            return destination
        item = source[counter]
        new_entry = item * counter
        return accumulate_result(accumulator, counter + 1, source, destination + [new_entry])

    return accumulate_result([], 1, array_of_values, []) if len(array_of_values) > 1 else []