def count_distinct_characters(input_string):
    lowercase_string = input_string.lower()
    unique_characters = set()
    for character in lowercase_string:
        unique_characters.add(character)
    distinct_count = len(unique_characters)
    return distinct_count