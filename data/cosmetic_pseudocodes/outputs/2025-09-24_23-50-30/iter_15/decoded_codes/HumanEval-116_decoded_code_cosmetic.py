from typing import List, Dict


def sort_array(array_of_integers: List[int]) -> List[int]:
    buffer_list: List[int] = array_of_integers[:]
    step_one: List[int] = []
    # Selection sort into step_one
    while buffer_list:
        min_element: int = buffer_list[0]
        for idx in range(len(buffer_list)):
            if buffer_list[idx] < min_element:
                min_element = buffer_list[idx]
        step_one.append(min_element)
        buffer_list = [el for el in buffer_list if el != min_element]

    def count_ones(number: int) -> int:
        count_accumulator: int = 0
        quotient_var = number
        while quotient_var > 0:
            remainder_var = quotient_var % 2
            quotient_var = (quotient_var - remainder_var) // 2
            if remainder_var != 0:
                count_accumulator += 1
        return count_accumulator

    step_two: List[int] = []
    processed_map: Dict[int, List[int]] = {}

    for element in step_one:
        key_value = count_ones(element)
        if key_value not in processed_map:
            processed_map[key_value] = []
        processed_map[key_value].append(element)

    final_result: List[int] = []
    sorted_keys: List[int] = sorted(processed_map.keys())
    index_var: int = 0
    while index_var < len(sorted_keys):
        for element in processed_map[sorted_keys[index_var]]:
            final_result.append(element)
        index_var += 1

    return final_result