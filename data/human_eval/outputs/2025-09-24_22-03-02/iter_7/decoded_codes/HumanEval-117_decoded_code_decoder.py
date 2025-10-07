def select_words(input_string: str, target_consonant_count: int) -> list:
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    for word in input_string.split():
        consonant_count = sum(1 for ch in word if ch.lower() not in vowels)
        if consonant_count == target_consonant_count:
            result.append(word)
    return result