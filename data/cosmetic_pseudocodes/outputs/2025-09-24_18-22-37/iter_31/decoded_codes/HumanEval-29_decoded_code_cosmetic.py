from typing import Iterable, List

def filter_by_prefix(sequence_of_words: Iterable[str], key_prefix: str) -> List[str]:
    collected_matches: List[str] = []
    for candidate_word in sequence_of_words:
        if candidate_word.startswith(key_prefix):
            collected_matches.append(candidate_word)
    return collected_matches