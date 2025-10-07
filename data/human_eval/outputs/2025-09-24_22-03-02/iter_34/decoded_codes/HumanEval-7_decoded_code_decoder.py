def filter_by_substring(strings, substring):
    filtered_list = []
    index = 0
    while index < len(strings):
        current_string = strings[index]
        contains_substring = False
        sub_index = 0
        while sub_index < len(current_string) - len(substring) + 1:
            match = True
            char_index = 0
            while char_index < len(substring):
                if current_string[sub_index + char_index] != substring[char_index]:
                    match = False
                    break
                char_index += 1
            if match:
                contains_substring = True
                break
            sub_index += 1
        if contains_substring:
            filtered_list.append(current_string)
        index += 1
    return filtered_list