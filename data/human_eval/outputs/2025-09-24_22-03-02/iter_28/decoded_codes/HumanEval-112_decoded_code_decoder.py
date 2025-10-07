def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    result_string = ""
    for index in range(len(s)):
        char = s[index]
        found = False
        for c_index in range(len(c)):
            if char == c[c_index]:
                found = True
                break
        if not found:
            result_string += char
    reversed_string = ""
    for rev_index in range(len(result_string) - 1, -1, -1):
        reversed_string += result_string[rev_index]
    is_palindrome = (reversed_string == result_string)
    return result_string, is_palindrome