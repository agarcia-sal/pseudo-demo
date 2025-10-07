def by_length(arr):
    # Dictionary mapping integers to their English names
    num_to_word = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Filter to include only elements between 1 and 9 inclusive
    filtered = [num for num in arr if 1 <= num <= 9]

    # Sort ascending then reverse to get descending order
    sorted_arr = sorted(filtered)[::-1]

    # Map numbers to words if they exist in the dictionary
    new_arr = [num_to_word[num] for num in sorted_arr if num in num_to_word]

    return new_arr