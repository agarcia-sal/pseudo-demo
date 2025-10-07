def histogram(test):
    # Initialize dictionary to store counts of most frequent words
    most_frequent = {}
    # Split the input string by spaces
    words = test.split()

    if not words:
        return most_frequent

    # Count occurrences of each word using a dictionary comprehension
    counts = {}
    for word in words:
        if word:
            counts[word] = counts.get(word, 0) + 1

    # Find the maximum count
    max_count = max(counts.values()) if counts else 0

    # Populate dictionary with words that have the maximum count
    if max_count > 0:
        for word, count in counts.items():
            if count == max_count:
                most_frequent[word] = count

    return most_frequent