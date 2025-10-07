def select_words(s, n):
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    for word in s.split():
        consonant_count = sum(1 for char in word if char.lower() not in vowels)
        if consonant_count == n:
            result.append(word)
    return result