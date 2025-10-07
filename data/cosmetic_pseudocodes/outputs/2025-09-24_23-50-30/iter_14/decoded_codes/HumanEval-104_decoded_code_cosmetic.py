from typing import List


def unique_digits(numbers: List[int]) -> List[int]:
    def collect_odd_digits(sequence: List[int], accumulator: List[int]) -> List[int]:
        if not sequence:
            return accumulator
        head, tail = sequence[0], sequence[1:]
        # Skip numbers containing any even digit
        if any((int(d) % 2 == 0) for d in str(head)):
            return collect_odd_digits(tail, accumulator)
        return collect_odd_digits(tail, accumulator + [head])

    result_list = collect_odd_digits(numbers, [])
    sorted_result: List[int] = []
    while result_list:
        min_val = result_list[0]
        for item in result_list:
            if item < min_val:
                min_val = item
        sorted_result.append(min_val)
        result_list = [x for x in result_list if x != min_val]
    return sorted_result