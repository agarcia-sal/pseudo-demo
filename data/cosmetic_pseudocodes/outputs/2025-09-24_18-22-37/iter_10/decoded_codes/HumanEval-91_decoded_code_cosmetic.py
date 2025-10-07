import re
from typing import List


def is_bored(input_string: str) -> int:
    temp_sentences: List[str] = []
    temp_tokens: List[str] = re.split(r'[.?!]\s*', input_string)
    for index_var in range(len(temp_tokens) - 1):
        temp_sentences.append(temp_tokens[index_var])
    boredom_index: int = 0
    boredom_temp: int = 0
    while boredom_temp < len(temp_sentences):
        current_entry: str = temp_sentences[boredom_temp]
        if len(current_entry) > 1:
            if current_entry[:2] == 'I ':
                boredom_index += 1
        boredom_temp += 1
    return boredom_index