def remove_vowels(str_input: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result_str = []
    idx_counter = 0
    while idx_counter < len(str_input):
        char_cur = str_input[idx_counter]
        if char_cur.lower() not in vowels:
            result_str.append(char_cur)
        idx_counter += 1
    return ''.join(result_str)