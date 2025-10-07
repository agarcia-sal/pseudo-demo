def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    filtered_characters = []
    index = 0
    while index < len(s):
        current_char = s[index]
        found_in_c = False
        index_c = 0
        while index_c < len(c):
            if current_char == c[index_c]:
                found_in_c = True
                break
            index_c += 1
        if not found_in_c:
            filtered_characters.append(current_char)
        index += 1
    s_filtered = ''
    index = 0
    while index < len(filtered_characters):
        s_filtered += filtered_characters[index]
        index += 1
    reversed_s = ''
    index = len(s_filtered) - 1
    while index >= 0:
        reversed_s += s_filtered[index]
        index -= 1
    is_palindrome = False
    if reversed_s == s_filtered:
        is_palindrome = True
    return s_filtered, is_palindrome