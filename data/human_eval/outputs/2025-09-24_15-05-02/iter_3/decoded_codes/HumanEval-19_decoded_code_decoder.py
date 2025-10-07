def sort_numbers(numbers: str) -> str:
    # Map number words to their corresponding numeric values
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Split the input string by spaces and filter out any empty strings
    list_of_words = [word for word in numbers.split(" ") if word]

    # Sort the list based on the numeric value from value_map
    sorted_list = sorted(list_of_words, key=lambda w: value_map[w])

    # Join the sorted words back into a single string separated by spaces
    sorted_string = " ".join(sorted_list)

    return sorted_string