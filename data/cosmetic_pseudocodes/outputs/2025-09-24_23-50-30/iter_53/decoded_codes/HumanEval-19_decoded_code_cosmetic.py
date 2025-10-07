from typing import List, Dict


def sort_numbers(parameter_alpha: str) -> str:
    variable_bravo: Dict[str, int] = {
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

    def helper_charlie(input_delta: List[str], accumulator_echo: List[str]) -> List[str]:
        if not input_delta:
            return accumulator_echo
        current_foxtrot, *rest_golf = input_delta
        if current_foxtrot == '':
            return helper_charlie(rest_golf, accumulator_echo)
        else:
            return helper_charlie(rest_golf, accumulator_echo + [current_foxtrot])

    variable_hotel: List[str] = helper_charlie(parameter_alpha.split(' '), [])

    def compare_india(juliet: str, kilo: str) -> bool:
        return variable_bravo[juliet] < variable_bravo[kilo]

    def merge_sort_lima(mike: List[str]) -> List[str]:
        if len(mike) <= 1:
            return mike
        midpoint_november = len(mike) // 2

        def merge_oscarr(papa: List[str], quebec: List[str]) -> List[str]:
            result_romeo: List[str] = []
            index_sierra = 0
            index_tango = 0
            while index_sierra < len(papa) and index_tango < len(quebec):
                if compare_india(papa[index_sierra], quebec[index_tango]):
                    result_romeo.append(papa[index_sierra])
                    index_sierra += 1
                else:
                    result_romeo.append(quebec[index_tango])
                    index_tango += 1
            result_romeo.extend(papa[index_sierra:])
            result_romeo.extend(quebec[index_tango:])
            return result_romeo

        left_uniform = merge_sort_lima(mike[:midpoint_november])
        right_victor = merge_sort_lima(mike[midpoint_november:])
        return merge_oscarr(left_uniform, right_victor)

    variable_whiskey = merge_sort_lima(variable_hotel)

    variable_xray = ' '.join(variable_whiskey)
    return variable_xray