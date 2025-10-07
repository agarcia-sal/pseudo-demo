def reverse_delete(input_string, chars_to_delete):
    filtered_string = ''.join(c for c in input_string if c not in chars_to_delete)
    return filtered_string, filtered_string == filtered_string[::-1]