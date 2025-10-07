def reverse_delete(s, c):
    filtered_string = ""
    for character in s:
        if character not in c:
            filtered_string += character
    is_palindrome = (filtered_string[::-1] == filtered_string)
    return (filtered_string, is_palindrome)