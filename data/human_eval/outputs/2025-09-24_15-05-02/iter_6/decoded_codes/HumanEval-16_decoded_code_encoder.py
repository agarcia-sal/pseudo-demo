def count_distinct_characters(string):
    lowercase_string = string.lower()
    unique_characters = set(lowercase_string)
    return len(unique_characters)