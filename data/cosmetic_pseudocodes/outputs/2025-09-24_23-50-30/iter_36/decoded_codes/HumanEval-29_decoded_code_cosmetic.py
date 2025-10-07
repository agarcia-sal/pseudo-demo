from typing import List

def does_not_start_with(main_text: str, test_prefix: str) -> bool:
    return not main_text.startswith(test_prefix)

def filter_by_prefix(array_of_texts: List[str], text_prefix: str) -> List[str]:
    collected_items: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(array_of_texts):
        if not does_not_start_with(array_of_texts[iterator_index], text_prefix):
            collected_items.append(array_of_texts[iterator_index])
        iterator_index += 1
    return collected_items