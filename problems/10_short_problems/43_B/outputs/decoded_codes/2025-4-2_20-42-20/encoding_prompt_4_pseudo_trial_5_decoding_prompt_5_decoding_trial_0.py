# Function to determine if the character frequency difference is non-negative between two input strings
def check_character_frequency():
    # Read two input strings
    input_string_1 = input()
    input_string_2 = input()

    # Remove spaces from both input strings
    cleaned_string_1 = input_string_1.replace(" ", "")
    cleaned_string_2 = input_string_2.replace(" ", "")

    # Initialize a frequency list to track the count difference of each character
    frequency_difference = [0] * 256  # ASCII characters range from 0 to 255

    # Calculate frequency difference for each character from ASCII value of 'A' to ASCII value of 'z'
    for character_code in range(65, 123):  # From ASCII 'A' (65) to 'z' (122)
        count_in_string_1 = cleaned_string_1.count(chr(character_code))
        count_in_string_2 = cleaned_string_2.count(chr(character_code))
        frequency_difference[character_code] = count_in_string_1 - count_in_string_2

    # Check if all frequency differences are non-negative
    if all(value >= 0 for value in frequency_difference[65:123]):  # Only checking range 'A' to 'z'
        print("YES")
    else:
        print("NO")

# Example test cases (uncomment to test)
# test input: "A B C" and "A B"
# check_character_frequency()  # Expected output: YES
