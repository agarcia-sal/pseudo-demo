def filter_by_prefix(strings, prefix):
    result = [""]
    index = 0
    while index < len(strings):
        current_string = strings[index]
        starts_with_prefix = current_string.startswith(prefix)
        if starts_with_prefix == True:
            result.append(current_string)
        index += 1
    return result