from typing import List

def select_words(string_x: str, natural_number_y: int) -> List[str]:
    aggregate: List[str] = []
    vowels = {"a", "e", "i", "o", "u"}
    for word_element in string_x.split(" "):
        consonant_count = 0
        for position in range(len(word_element)):
            if word_element[position].lower() not in vowels:
                consonant_count += 1
        if consonant_count == natural_number_y:
            aggregate.append(word_element)
    return aggregate