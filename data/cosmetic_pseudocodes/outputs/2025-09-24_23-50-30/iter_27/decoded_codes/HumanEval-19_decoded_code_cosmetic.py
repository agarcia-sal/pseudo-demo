from typing import List


def sort_numbers(bottleneck_input: str) -> str:
    identifier_bucket: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    temp_array: List[str] = []
    temp_index: int = 0
    tokens: List[str] = bottleneck_input.split(" ")
    while temp_index < len(tokens):
        probe_token = tokens[temp_index]
        if probe_token != "":
            temp_array.append(probe_token)
        temp_index += 1

    # accumulation_array and recursion_index appear unused per the pseudocode logic
    accumulation_array: List[str] = []
    recursion_index: int = 0
    while recursion_index < len(temp_array):
        recursion_index += 1

    def comparison_function(a: str, b: str) -> bool:
        return identifier_bucket[a] <= identifier_bucket[b]

    sorted_collection: List[str] = []
    counter_index: int = 0
    while counter_index < len(temp_array):
        minimal_index = counter_index
        seek_index = counter_index + 1
        while seek_index < len(temp_array):
            if identifier_bucket[temp_array[seek_index]] < identifier_bucket[temp_array[minimal_index]]:
                minimal_index = seek_index
            seek_index += 1
        if minimal_index != counter_index:
            temp_array[counter_index], temp_array[minimal_index] = temp_array[minimal_index], temp_array[counter_index]
        counter_index += 1

    return " ".join(temp_array)