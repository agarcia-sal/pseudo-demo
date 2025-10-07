def is_palindrome(text: str) -> bool:
    length_of_text = len(text)
    i = 0
    while i < length_of_text:
        front_character = text[i]
        back_index = length_of_text - 1 - i
        back_character = text[back_index]
        if front_character != back_character:
            return False
        i += 1
    return True