def count_distinct_characters(string: str) -> int:
    lower_string = ""
    index = 0
    while index < len(string):
        lower_char = string[index].lower()
        lower_string += lower_char
        index += 1
    distinct_characters = [""]
    index = 0
    while index < len(lower_string):
        current_char = lower_string[index]
        found = False
        check_index = 0
        while check_index < len(distinct_characters):
            if distinct_characters[check_index] == current_char:
                found = True
                break
            check_index += 1
        if found == False:
            distinct_characters.append(current_char)
        index += 1
    return len(distinct_characters)