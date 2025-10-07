def select_words(s, n):
    result = []
    vowels = {"a", "e", "i", "o", "u"}
    for word in s.split():
        consonant_count = 0
        for char in word:
            if char.lower() not in vowels:
                consonant_count += 1
        if consonant_count == n:
            result.append(word)
    return result