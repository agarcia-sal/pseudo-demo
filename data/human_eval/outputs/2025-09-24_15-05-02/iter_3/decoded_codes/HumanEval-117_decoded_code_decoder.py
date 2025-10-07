def select_words(s, n):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for word in s.split():
        # Count consonants in the word
        consonant_count = sum(1 for char in word.lower() if char.isalpha() and char not in vowels)
        if consonant_count == n:
            result.append(word)
    return result