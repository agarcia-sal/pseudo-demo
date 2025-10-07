def reverse_delete(string_s: str, string_c: str) -> tuple[str, bool]:
    filtered_string = ""
    for character in string_s:
        if character not in string_c:
            filtered_string += character
    is_palindrome = filtered_string == filtered_string[::-1]
    return filtered_string, is_palindrome