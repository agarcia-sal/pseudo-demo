def count_distinct_characters(string: str) -> int:
    lowercase_string = ""
    i = 0
    while i < len(string):
        current_char = string[i]
        if 'A' <= current_char <= 'Z':
            lowercase_char = current_char.lower()
        else:
            lowercase_char = current_char
        lowercase_string += lowercase_char
        i += 1
    distinct_chars = []
    j = 0
    while j < len(lowercase_string):
        char_j = lowercase_string[j]
        found = False
        k = 0
        while k < len(distinct_chars):
            if distinct_chars[k] == char_j:
                found = True
                break
            k += 1
        if not found:
            distinct_chars.append(char_j)
        j += 1
    return len(distinct_chars)