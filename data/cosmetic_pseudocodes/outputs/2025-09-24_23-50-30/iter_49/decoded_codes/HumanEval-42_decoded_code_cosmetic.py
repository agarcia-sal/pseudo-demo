from typing import List

def incr_list(container_of_units: List[int]) -> List[int]:

    def reap_altered_indexed(set_of_values: List[int], index_counter: int, output_list: List[int]) -> List[int]:
        if index_counter == len(set_of_values):
            return output_list
        accumulated_value = set_of_values[index_counter] + 1
        output_list.append(accumulated_value)
        return reap_altered_indexed(set_of_values, index_counter + 1, output_list)

    return reap_altered_indexed(container_of_units, 0, [])