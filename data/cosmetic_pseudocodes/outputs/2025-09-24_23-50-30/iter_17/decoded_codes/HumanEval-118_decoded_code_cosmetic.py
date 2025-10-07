from typing import Dict

def get_closest_vowel(text: str) -> str:
    if len(text) < 3:
        return ""

    vowel_collection: Dict[str, bool] = {v: True for v in "aeiouAEIOU"}

    position = len(text) - 2
    while position >= 1:
        if vowel_collection.get(text[position], False):
            if not vowel_collection.get(text[position + 1], False) and not vowel_collection.get(text[position - 1], False):
                return text[position]
        position -= 1

    return ""