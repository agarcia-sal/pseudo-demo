def fruit_distribution(s: str, n: int) -> int:
    # Extract integer numbers from string s
    list_of_numbers = [int(word) for word in s.split() if word.isdigit()]
    # Calculate the result by subtracting the sum of extracted numbers from n
    return n - sum(list_of_numbers)