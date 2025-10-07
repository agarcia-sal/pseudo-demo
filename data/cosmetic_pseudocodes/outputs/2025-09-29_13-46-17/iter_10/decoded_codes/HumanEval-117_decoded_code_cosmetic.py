from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    selected_words: List[str] = []
    for word in string_s.split(" "):
        vowel_count = 0
        for i in range(len(word)):
            ch = word[i].lower()
            if ch not in ("a", "e", "i", "o", "u"):
                vowel_count += 1
        if vowel_count == natural_number_n:
            selected_words.append(word)
    return selected_words