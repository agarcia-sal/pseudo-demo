def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    result_string = ''.join(char for char in s if char not in c)
    length = len(result_string)
    is_palindrome = True
    index = 0
    while index < length // 2:
        if result_string[index] != result_string[length - 1 - index]:
            is_palindrome = False
            break
        index += 1
    return result_string, is_palindrome