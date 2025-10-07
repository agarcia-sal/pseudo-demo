from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    pieces = input_text.split(' ')
    max_freq = 0
    idx = 0

    while idx < len(pieces):
        current_elem = pieces[idx]
        current_freq = 0
        jdx = 0

        while jdx < len(pieces):
            if pieces[jdx] == current_elem:
                current_freq += 1
            jdx += 1

        if current_freq > max_freq and current_elem != '':
            max_freq = current_freq
        idx += 1

    if max_freq > 0:
        kdx = 0
        while kdx < len(pieces):
            letter_at_k = pieces[kdx]
            freq_of_letter = 0
            ldx = 0

            while ldx < len(pieces):
                if pieces[ldx] == letter_at_k:
                    freq_of_letter += 1
                ldx += 1

            if freq_of_letter == max_freq:
                freq_map[letter_at_k] = max_freq
            kdx += 1

    return freq_map