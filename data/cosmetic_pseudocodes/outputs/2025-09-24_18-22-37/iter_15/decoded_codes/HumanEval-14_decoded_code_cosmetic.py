from typing import List

def all_prefixes(alternative_input: str) -> List[str]:
    transformed_collection: List[str] = []
    numeric_counter: int = 0
    while numeric_counter <= len(alternative_input) - 1:
        boundary_length: int = numeric_counter + 1
        partial_extraction: str = alternative_input[0:boundary_length]
        transformed_collection.append(partial_extraction)
        numeric_counter += 1
    return transformed_collection