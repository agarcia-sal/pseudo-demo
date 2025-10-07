from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_collection: List[str] = []
    current_index: int = 0
    total_elements: int = len(list_of_strings)

    while current_index < total_elements:
        candidate: str = list_of_strings[current_index]
        substring_present: bool = False
        candidate_length: int = len(candidate)
        substring_length: int = len(substring_value)
        position: int = 0
        max_position: int = candidate_length - substring_length

        while position <= max_position and not substring_present:
            segment: str = ""
            offset: int = 0
            while offset < substring_length:
                segment += candidate[position + offset]
                offset += 1
            if segment == substring_value:
                substring_present = True
            position += 1

        if substring_present:
            filtered_collection.append(candidate)

        current_index += 1

    return filtered_collection