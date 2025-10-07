def vowels_count(str_val: str) -> int:
    vowels_list: str = "aeiouAEIOU"
    count_vowels: int = 0
    for char in str_val:
        if char in vowels_list:
            count_vowels += 1
    if str_val and str_val[-1] in ('y', 'Y'):
        count_vowels += 1
    return count_vowels