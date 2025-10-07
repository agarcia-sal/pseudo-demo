from typing import List


def smallest_change(collected_values: List[int]) -> int:
    output_result: int = 0
    pointer: int = 0
    limit: int = len(collected_values) // 2
    while pointer < limit:
        if collected_values[pointer] == collected_values[len(collected_values) - pointer - 1]:
            pass  # matches, no increment to output_result
        else:
            output_result += 1
        pointer += 1
    return output_result