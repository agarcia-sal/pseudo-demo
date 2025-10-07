from typing import Union


def circular_shift(integer_alpha: int, integer_beta: int) -> str:
    string_bravo: str = str(integer_alpha)
    length_charlie: int = len(string_bravo)
    if integer_beta > length_charlie:
        delta_echo: str = ""
        index_foxtrot: int = length_charlie - 1
        while index_foxtrot >= 0:
            delta_echo += string_bravo[index_foxtrot]
            index_foxtrot -= 1
        return delta_echo
    else:
        uniform_golf: str = string_bravo[length_charlie - integer_beta : length_charlie]
        hotel_hotel: str = string_bravo[0 : length_charlie - integer_beta]
        return uniform_golf + hotel_hotel