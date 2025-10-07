from typing import List

def f(integer_n: int) -> List[int]:
    output_collection: List[int] = []

    def process_index_rec(current_index: int) -> None:
        if current_index % 2 == 0:
            temp_accumulator = 1
            temp_multiplier = 1
            while temp_multiplier <= current_index:
                temp_accumulator *= temp_multiplier
                temp_multiplier += 1
            temp_result = temp_accumulator
        else:
            temp_accumulator = 0
            temp_adder = 1
            while temp_adder <= current_index:
                temp_accumulator += temp_adder
                temp_adder += 1
            temp_result = temp_accumulator

        output_collection.append(temp_result)
        if current_index < integer_n:
            process_index_rec(current_index + 1)

    process_index_rec(1)
    return output_collection