def count_distinct_characters(input_string):
    lowercase_string = input_string.lower()
    distinct_characters = set(lowercase_string)
    return len(distinct_characters)