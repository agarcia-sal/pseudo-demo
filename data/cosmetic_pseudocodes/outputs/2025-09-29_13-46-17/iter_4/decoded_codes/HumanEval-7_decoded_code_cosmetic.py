from typing import List

def filter_by_substring(inputStrings: List[str], targetPattern: str) -> List[str]:
    result_collection: List[str] = []
    current_index: int = 0

    while current_index < len(inputStrings):
        if targetPattern in inputStrings[current_index]:
            result_collection.append(inputStrings[current_index])
        current_index += 1

    return result_collection