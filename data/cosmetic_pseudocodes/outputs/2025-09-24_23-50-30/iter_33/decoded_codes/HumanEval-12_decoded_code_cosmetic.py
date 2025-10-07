from typing import Optional, Sequence

def longest(sequence_of_texts: Sequence[str]) -> Optional[str]:
    def find_max_length(acc: int, items: Sequence[str]) -> int:
        if not items:
            return acc
        head_text, *tail_texts = items
        return find_max_length(acc if acc > len(head_text) else len(head_text), tail_texts)

    if sequence_of_texts:
        max_len = find_max_length(0, sequence_of_texts)
        for candidate_text in sequence_of_texts:
            if len(candidate_text) == max_len:
                return candidate_text
    else:
        return None