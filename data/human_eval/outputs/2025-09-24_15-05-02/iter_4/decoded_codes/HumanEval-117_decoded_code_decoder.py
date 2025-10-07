def select_words(s, n):
    result = []
    vowels = {"a", "e", "i", "o", "u"}
    for word in s.split():
        number_of_consonants = 0
        for char in word:
            if char.lower() not in vowels:
                number_of_consonants += 1
        if number_of_consonants == n:
            result.append(word)
    return result