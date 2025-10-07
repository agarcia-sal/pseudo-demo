def count_distinct_characters(string: str) -> int:
    lower_string = string.lower()
    unique_characters = []
    index = 0
    while index < len(lower_string):
        current_character = lower_string[index]
        found = False
        check_index = 0
        while check_index < len(unique_characters):
            if unique_characters[check_index] == current_character:
                found = True
                break
            check_index += 1
        if not found:
            unique_characters.append(current_character)
        index += 1
    return len(unique_characters)