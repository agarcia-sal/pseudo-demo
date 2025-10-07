from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []
    aggregate_collection = ((" " if c == "," else c) for c in input_string)
    combined_string = "".join(aggregate_collection)
    return combined_string.split()