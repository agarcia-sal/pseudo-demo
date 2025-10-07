def reverse_delete(string_s, string_c):
    filtered_string = ''.join(char for char in string_s if char not in string_c)
    return filtered_string, filtered_string == filtered_string[::-1]