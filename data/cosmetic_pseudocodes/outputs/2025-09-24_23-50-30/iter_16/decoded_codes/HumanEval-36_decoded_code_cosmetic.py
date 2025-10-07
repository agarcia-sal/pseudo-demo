from typing import Dict

def fizz_buzz(integer_n: int) -> int:
    def gather_multiples(current_index: int, collected_map: Dict[int, bool]) -> Dict[int, bool]:
        if current_index == integer_n:
            return collected_map
        divisible_by_11 = (current_index % 11) == 0 and current_index != 0
        divisible_by_13 = (current_index % 13) == 0 and current_index != 0
        if divisible_by_11 or divisible_by_13:
            collected_map[current_index] = True
        return gather_multiples(current_index + 1, collected_map)

    def build_string(keys_map: Dict[int, bool], acc_str: str) -> str:
        if not keys_map:
            return acc_str
        # Remove one item arbitrarily
        head_key, _ = keys_map.popitem()
        return build_string(keys_map, acc_str + str(head_key))

    def count_character(string_to_search: str, char_target: str, idx: int, count_accum: int) -> int:
        if idx >= len(string_to_search):
            return count_accum
        return count_character(
            string_to_search,
            char_target,
            idx + 1,
            count_accum + (1 if string_to_search[idx] == char_target else 0)
        )

    multiples_map: Dict[int, bool] = gather_multiples(0, {})
    composite_string = build_string(multiples_map, "")
    return count_character(composite_string, '7', 0, 0)