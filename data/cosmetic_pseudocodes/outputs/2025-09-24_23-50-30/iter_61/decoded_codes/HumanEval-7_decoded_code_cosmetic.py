from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    def recursive_filter(
        source_list: List[str],
        filter_value: str,
        position_index: int,
        accumulator_list: List[str],
    ) -> List[str]:
        if position_index >= len(source_list):
            return accumulator_list

        current_element = source_list[position_index]
        includes_substring = False

        # Switch true pattern for substring inclusion check
        if filter_value in current_element:
            includes_substring = True
        else:
            includes_substring = False

        if includes_substring:
            return recursive_filter(
                source_list, filter_value, position_index + 1, accumulator_list + [current_element]
            )
        else:
            return recursive_filter(
                source_list, filter_value, position_index + 1, accumulator_list
            )

    return recursive_filter(list_of_strings, substring_value, 0, [])