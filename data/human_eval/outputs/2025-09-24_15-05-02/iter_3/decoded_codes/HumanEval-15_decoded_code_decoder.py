def string_sequence(n: int) -> str:
    # Generate a list of string representations of numbers from 0 to n inclusive
    list_of_strings = [str(x) for x in range(n + 1)]
    # Join the list into a single string with spaces separating the numbers
    return ' '.join(list_of_strings)