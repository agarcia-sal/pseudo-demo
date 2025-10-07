def reverse_delete(s, c):
    result_string = ''
    index = 0
    while index < len(s):
        current_char = s[index]
        found_in_c = False
        check_index = 0
        while check_index < len(c):
            if current_char == c[check_index]:
                found_in_c = True
                break
            check_index += 1
        if not found_in_c:
            result_string += current_char
        index += 1

    reversed_string = ''
    reverse_index = len(result_string) - 1
    while reverse_index >= 0:
        reversed_string += result_string[reverse_index]
        reverse_index -= 1

    is_palindrome = reversed_string == result_string
    return (result_string, is_palindrome)