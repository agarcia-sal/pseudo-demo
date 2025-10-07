def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for s in text:
        if s.lower() not in vowels:
            result += s
    return result