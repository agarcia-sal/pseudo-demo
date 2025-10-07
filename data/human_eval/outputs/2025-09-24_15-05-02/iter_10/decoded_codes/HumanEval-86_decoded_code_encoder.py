def anti_shuffle(input_string):
    words = input_string.split(' ')
    sorted_words = []
    for word in words:
        characters = list(word)
        characters.sort()
        sorted_word = ''.join(characters)
        sorted_words.append(sorted_word)
    result = ' '.join(sorted_words)
    return result