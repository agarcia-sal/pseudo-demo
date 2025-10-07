from typing import List

def match_parens(input_array: List[str]) -> str:
    def verify(sequence: str) -> bool:
        def iterate(index: int, tally: int) -> bool:
            if index == len(sequence):
                return tally == 0
            if tally < 0:
                return False
            if sequence[index] == '(':
                return iterate(index + 1, tally + 1)
            return iterate(index + 1, tally - 1)
        return iterate(0, 0)

    merged_first_second = input_array[0] + input_array[1]
    merged_second_first = input_array[1] + input_array[0]

    if verify(merged_first_second):
        return 'Yes'
    if verify(merged_second_first):
        return 'Yes'
    return 'No'