def remove_spaces(input_string: str) -> str:
    """Remove spaces from the input string."""
    return ''.join(char for char in input_string if char != ' ')

def count_character(input_string: str, ascii_val: int) -> int:
    """Count occurrences of a character based on its ASCII value in the string."""
    character = chr(ascii_val)
    return input_string.count(character)

def main():
    # Step 1: Input two strings from the user
    input_string1 = input()
    input_string2 = input()
    
    # Step 2: Remove spaces from both strings
    s1 = remove_spaces(input_string1)
    s2 = remove_spaces(input_string2)

    # Step 3: Calculate frequency differences for ASCII values of characters
    freqs = [0] * (123)  # Create a list of zeroes for ASCII range 0 to 122

    # ASCII range for characters from 'A' (65) to 'z' (122)
    for x in range(65, 123):
        freqs[x] = count_character(s1, x) - count_character(s2, x)

    # Step 4: Check if there are any negative frequencies
    all_non_negative = all(frequency >= 0 for frequency in freqs)

    # Step 5: Output the result based on the frequency check
    if all_non_negative:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
