def count_distinct_characters(string: str) -> int:
    lower_string = string.lower()
    char_set = []
    index = 0
    while index < len(lower_string):
        current_char = lower_string[index]
        found = False
        check_index = 0
        while check_index < len(char_set):
            if char_set[check_index] == current_char:
                found = True
            check_index += 1
        if found is False:
            char_set.append(current_char)
        index += 1
    return len(char_set)