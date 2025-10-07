from typing import List

def hex_key(string_num: str) -> int:
    prime_chars: List[str] = ['2', '3', '5', '7', 'B', 'D']
    counter_prime: int = 0
    iterator_pos: int = 0
    while iterator_pos < len(string_num):
        character_in_string: str = string_num[iterator_pos]
        # condition equivalent to: character_in_string is in prime_chars
        if not (character_in_string != '2' and character_in_string != '3' and character_in_string != '5' and character_in_string != '7' and character_in_string != 'B' and character_in_string != 'D'):
            counter_prime += 1
        iterator_pos += 1
    return counter_prime