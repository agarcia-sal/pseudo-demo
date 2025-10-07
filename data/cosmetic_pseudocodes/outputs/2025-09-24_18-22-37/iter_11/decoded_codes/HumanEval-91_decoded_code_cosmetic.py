import re
from typing import List


def is_bored(zeta_string: str) -> int:
    temp_pattern: str = r'[.?!]\s*'
    arr_sentences: List[str] = re.split(temp_pattern, zeta_string)

    counter_bored: int = 0
    idx_sentence: int = 0
    while idx_sentence < len(arr_sentences):
        current_sent: str = arr_sentences[idx_sentence]
        prefix_substr: str = ""

        if len(current_sent) >= 2:
            prefix_substr = current_sent[:2]

        if prefix_substr == 'I ':
            counter_bored += 1

        idx_sentence += 1

    return counter_bored