from typing import List, Dict

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    def build_counter(accumulator: Dict[int, int], items: List[int]) -> Dict[int, int]:
        if not items:
            return accumulator
        current_item = items[0]
        remaining_items = items[1:]
        updated_accumulator = dict(accumulator)
        updated_accumulator[current_item] = updated_accumulator.get(current_item, 0) + 1
        return build_counter(updated_accumulator, remaining_items)

    def auxiliary(seq: List[int], tab: Dict[int, int]) -> List[int]:
        if not seq:
            return []
        head_chunk = seq[0]
        tail_chunk = seq[1:]
        count_value = tab.get(head_chunk, 0)
        if not (count_value > 1):
            return [head_chunk] + auxiliary(tail_chunk, tab)
        else:
            return auxiliary(tail_chunk, tab)

    frequency_map = build_counter({}, list_of_numbers)
    return auxiliary(list_of_numbers, frequency_map)