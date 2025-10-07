def reverse_delete(s: str, c: str) -> tuple:
    result = ""
    for char in s:
        if char not in c:
            result += char
    is_palindrome = (result == result[::-1])
    return (result, is_palindrome)