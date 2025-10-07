def anti_shuffle(s):
    # Split the input string into words
    list_of_words = s.split()

    # For each word, sort the characters by ASCII value and collect the results
    ordered_words = [''.join(sorted(word)) for word in list_of_words]

    # Join the processed words back into a single string separated by spaces
    return ' '.join(ordered_words)