def process_string(input_string):
    """Remove spaces from the input string and return the processed version."""
    return input_string.replace(" ", "")

def calculate_frequency_difference(first_processed, second_processed):
    """Calculate the frequency difference of characters from first_processed to second_processed."""
    frequency_difference = [0] * 128  # ASCII range from 0 to 127
    for char in first_processed:
        frequency_difference[ord(char)] += 1
    for char in second_processed:
        frequency_difference[ord(char)] -= 1
    return frequency_difference

def check_character_frequencies(first_string, second_string):
    """Check if first_string meets or exceeds the character frequencies of second_string."""
    first_processed = process_string(first_string)
    second_processed = process_string(second_string)
    
    frequency_difference = calculate_frequency_difference(first_processed, second_processed)

    # Check for negative values indicating insufficient characters
    if all(diff >= 0 for diff in frequency_difference):
        print("YES")
    else:
        print("NO")

# Main execution
if __name__ == "__main__":
    first_string = input()
    second_string = input()
    check_character_frequencies(first_string, second_string)
