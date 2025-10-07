from typing import Collection

def concatenate(collection_of_texts: Collection[str]) -> str:
    result_text: str = ""
    index: int = 0
    while index < len(collection_of_texts):
        current_text: str = list(collection_of_texts)[index]
        result_text += current_text
        index += 1
    return result_text