def reverse_delete(s: str, c: str):
    filtered_string = ''.join(char for char in s if char not in c)
    is_palindrome = filtered_string == filtered_string[::-1]
    return filtered_string, is_palindrome