from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    total_elements_count = len(sequence_of_values)
    if total_elements_count == 0:
        raise ValueError("sequence_of_values must not be empty")
    accumulator_sum = 0.0
    index_counter = 0
    while index_counter < total_elements_count:
        accumulator_sum += sequence_of_values[index_counter]
        index_counter += 1
    average_result = accumulator_sum / total_elements_count
    aggregate_deviation = 0.0
    loop_pointer = 0
    while loop_pointer < total_elements_count:
        if sequence_of_values[loop_pointer] >= average_result:
            aggregate_deviation += sequence_of_values[loop_pointer] - average_result
        else:
            aggregate_deviation += average_result - sequence_of_values[loop_pointer]
        loop_pointer += 1
    FINAL_RESULT = aggregate_deviation / total_elements_count
    return FINAL_RESULT