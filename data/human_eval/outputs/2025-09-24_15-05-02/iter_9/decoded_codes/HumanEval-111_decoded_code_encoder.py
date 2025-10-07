def histogram(test):
    frequency_dict = {}
    words = test.split(' ')
    max_count = 0

    for word in words:
        if word != '':
            count = words.count(word)
            if count > max_count:
                max_count = count

    if max_count > 0:
        for word in words:
            if words.count(word) == max_count:
                frequency_dict[word] = max_count

    return frequency_dict