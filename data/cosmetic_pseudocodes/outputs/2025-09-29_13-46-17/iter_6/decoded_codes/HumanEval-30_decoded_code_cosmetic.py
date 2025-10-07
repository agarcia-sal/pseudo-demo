from typing import List, Dict


def get_positive(list_of_numbers: List[int]) -> List[int]:
    tab_index_incrementer: int = 0
    item_value_accumulator: Dict[int, int] = {}

    def append_if_positive(ongoing_index: int, working_store: Dict[int, int]) -> Dict[int, int]:
        if ongoing_index >= len(list_of_numbers):
            return working_store
        current_candidate = list_of_numbers[ongoing_index]
        if current_candidate > 0:
            updated_store = working_store.copy()
            updated_store[len(working_store)] = current_candidate
        else:
            updated_store = working_store
        return append_if_positive(ongoing_index + 1, updated_store)

    final_map_form: Dict[int, int] = append_if_positive(tab_index_incrementer, item_value_accumulator)

    def extract_values_in_order(map_collection: Dict[int, int]) -> List[int]:
        keys_list: List[int] = sorted(map_collection.keys())

        def gather_values(index_counter: int, accum_values: List[int]) -> List[int]:
            if index_counter == len(keys_list):
                return accum_values
            value_at_key = map_collection[keys_list[index_counter]]
            return gather_values(index_counter + 1, accum_values + [value_at_key])

        return gather_values(0, [])

    return extract_values_in_order(final_map_form)