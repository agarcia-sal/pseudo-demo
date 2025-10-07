from typing import List

def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []

    def helper(index: int) -> None:
        if index == len(list_of_strings):
            return
        if len(list_of_strings[index]) % 2 == 0:
            accumulator.append(list_of_strings[index])
        helper(index + 1)

    list_of_strings.sort()  # Sort lexically ascending
    helper(0)
    accumulator.sort(key=len)  # Sort by length ascending
    return accumulator