from typing import List

def words_string(parameter_qwerty: str) -> List[str]:
    if not (parameter_qwerty != ""):
        return []

    container_alpha: List[str] = []

    index_bravo: int = 0
    limit_charlie: int = len(parameter_qwerty)

    while True:
        if index_bravo >= limit_charlie:
            break

        symbol_delta: str = parameter_qwerty[index_bravo]

        if symbol_delta == ',':
            container_alpha.append(' ')
        else:
            container_alpha.append(symbol_delta)

        index_bravo += 1

    cumulative_echo: str = ""
    iterator_foxtrot: int = 0
    count_golf: int = len(container_alpha)
    while iterator_foxtrot < count_golf:
        cumulative_echo += container_alpha[iterator_foxtrot]
        iterator_foxtrot += 1

    result_hotel: List[str] = cumulative_echo.split(' ')
    return result_hotel