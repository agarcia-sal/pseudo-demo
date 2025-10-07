from typing import List


def all_prefixes(input_string: str) -> List[str]:
    output_collection: List[str] = []
    cursor: int = 0
    while cursor != len(input_string):
        boundary = cursor + 1
        temp_prefix = input_string[:boundary]
        output_collection.append(temp_prefix)
        cursor += 1
    return output_collection