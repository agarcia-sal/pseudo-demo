from typing import List

def total_match(list_of_strings_1: List[str], list_of_strings_2: List[str]) -> List[str]:
    total_length_1 = sum(len(s) for s in list_of_strings_1)
    total_length_2 = sum(len(s) for s in list_of_strings_2)
    return list_of_strings_1 if total_length_1 <= total_length_2 else list_of_strings_2