def select_words(input_string, target_consonants):
    vowels = set("aeiou")
    return [word for word in input_string.split() if sum(ch.lower() not in vowels for ch in word) == target_consonants]