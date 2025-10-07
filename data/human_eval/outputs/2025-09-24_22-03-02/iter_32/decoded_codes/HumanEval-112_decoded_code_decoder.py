def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    filtered_chars = []
    for index in range(len(s)):
        char = s[index]
        found_in_c = False
        for c_index in range(len(c)):
            if char == c[c_index]:
                found_in_c = True
                break
        if not found_in_c:
            filtered_chars.append(char)
    s = ''
    for index in range(len(filtered_chars)):
        s += filtered_chars[index]
    reversed_s = ''
    for index in range(len(s)-1, -1, -1):
        reversed_s += s[index]
    is_palindrome = False
    if reversed_s == s:
        is_palindrome = True
    return (s, is_palindrome)