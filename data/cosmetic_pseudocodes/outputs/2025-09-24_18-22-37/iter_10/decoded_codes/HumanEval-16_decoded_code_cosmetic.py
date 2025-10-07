def count_distinct_characters(observed_string: str) -> int:
    transformed_string: str = observed_string.lower()
    characters_collection: set[str] = set(transformed_string)
    result_value: int = len(characters_collection)
    return result_value