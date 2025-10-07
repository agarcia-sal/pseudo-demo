def count_distinct_characters(input_string: str) -> int:
    temp_collection = input_string.lower()
    unique_elements = set()
    position = 0

    while position < len(temp_collection):
        unique_elements.add(temp_collection[position])
        position += 1

    return len(unique_elements)