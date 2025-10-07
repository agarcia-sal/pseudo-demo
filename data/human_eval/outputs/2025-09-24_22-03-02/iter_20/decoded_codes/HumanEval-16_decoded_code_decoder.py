def count_distinct_characters(string: str) -> int:
    lower_string = []
    index = 0
    while index < len(string):
        lower_string.append(string[index].lower())
        index += 1
    distinct_characters = []
    index_lower = 0
    while index_lower < len(lower_string):
        current_char = lower_string[index_lower]
        is_new = True
        index_distinct = 0
        while index_distinct < len(distinct_characters):
            if distinct_characters[index_distinct] == current_char:
                is_new = False
                break
            index_distinct += 1
        if is_new:
            distinct_characters.append(current_char)
        index_lower += 1
    return len(distinct_characters)