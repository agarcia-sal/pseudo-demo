from typing import List

def string_sequence(integer_n: int) -> str:
    def helper(index: int, accumulator: List[str]) -> List[str]:
        if index > integer_n:
            return accumulator
        def convert_and_append(value: int, collection: List[str]) -> List[str]:
            return collection + [str(value)]
        return helper(index + 1, convert_and_append(index, accumulator))

    sequence_list = helper(0, [])
    output = ""
    for i in range(len(sequence_list)):
        output += sequence_list[i]
        if i < len(sequence_list) - 1:
            output += " "
    return output