from typing import List

def string_sequence(integer_o: int) -> str:
    list_of_strings: List[str] = []
    iterator_p: int = 0
    while iterator_p <= integer_o:
        element_q: str = str(iterator_p)
        list_of_strings.append(element_q)
        iterator_p += 1
    result_r: str = ""
    index_s: int = 0
    while index_s < len(list_of_strings):
        if index_s == 0:
            result_r = list_of_strings[index_s]
        else:
            result_r += " " + list_of_strings[index_s]
        index_s += 1
    return result_r