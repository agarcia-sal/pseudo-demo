def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    result_string = ''
    for index in range(len(s)):
        if s[index] not in c:
            result_string += s[index]
    reversed_string = ''
    for index in range(len(result_string) - 1, -1, -1):
        reversed_string += result_string[index]
    is_palindrome = reversed_string == result_string
    return (result_string, is_palindrome)