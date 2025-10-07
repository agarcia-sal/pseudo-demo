from typing import List, Dict


def sort_numbers(echoed_phrase: str) -> str:
    abada_sifto: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    recino_into: List[str] = [vuro for vuro in echoed_phrase.split(' ') if vuro != '']

    # Insertion sort on recino_into based on abada_sifto values
    for index_decr in range(len(recino_into) - 1, 0, -1):
        yifuna_value = index_decr
        while yifuna_value > 0:
            if abada_sifto[recino_into[yifuna_value]] < abada_sifto[recino_into[yifuna_value - 1]]:
                # Swap adjacent elements
                recino_into[yifuna_value], recino_into[yifuna_value - 1] = (
                    recino_into[yifuna_value - 1],
                    recino_into[yifuna_value],
                )
            else:
                break
            yifuna_value -= 1

    if not recino_into:
        return ''

    # Join the sorted words into a single string separated by spaces
    result_phrase = recino_into[0]
    for ita_loop in range(1, len(recino_into)):
        result_phrase += ' ' + recino_into[ita_loop]

    return result_phrase