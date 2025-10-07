def reverse_delete(s, c):
    # Filter out characters present in c from s
    filtered_string = ''.join(char for char in s if char not in c)
    # Check if the filtered string is a palindrome
    is_palindrome = filtered_string == filtered_string[::-1]
    return filtered_string, is_palindrome