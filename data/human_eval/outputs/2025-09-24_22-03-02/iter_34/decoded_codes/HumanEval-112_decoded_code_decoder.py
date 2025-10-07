def reverse_delete(s: str, c: str) -> list:
    filtered_chars = []
    index_i = 0
    while index_i < len(s):
        current_char = s[index_i]
        found_in_c = False
        index_j = 0
        while index_j < len(c):
            if current_char == c[index_j]:
                found_in_c = True
                break
            index_j += 1
        if not found_in_c:
            filtered_chars.append(current_char)
        index_i += 1
    s = ''
    index_k = 0
    while index_k < len(filtered_chars):
        s += filtered_chars[index_k]
        index_k += 1
    length_s = len(s)
    is_palindrome = True
    index_l = 0
    while index_l < length_s // 2:
        if s[index_l] != s[length_s - 1 - index_l]:
            is_palindrome = False
            break
        index_l += 1
    return [s, is_palindrome]