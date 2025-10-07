def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for s in text:
        if s.lower() not in vowels:
            result.append(s)
    joined_result = "".join(result)
    return joined_result