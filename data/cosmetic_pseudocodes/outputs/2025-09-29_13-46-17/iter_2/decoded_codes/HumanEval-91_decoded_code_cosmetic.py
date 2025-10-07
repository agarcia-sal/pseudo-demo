import re
from typing import List

def is_bored(input_string: str) -> int:
    def count_prefixes(sentences: List[str], idx: int, acc: int) -> int:
        if idx >= len(sentences):
            return acc
        current_sentence = sentences[idx]
        prefix_check = current_sentence.startswith('I ')
        new_acc = acc + (1 if prefix_check else 0)
        return count_prefixes(sentences, idx + 1, new_acc)

    sentence_array = re.split(r'[.?!]\s*', input_string)
    return count_prefixes(sentence_array, 0, 0)