def count_distinct_characters(parameter_one: str) -> int:
    temp_string: str = parameter_one.lower()
    char_collection: set[str] = set()
    for index_var in range(len(temp_string)):
        char_item: str = temp_string[index_var]
        char_collection |= {char_item}  # union with single-element set
    distinct_count: int = len(char_collection)
    return distinct_count