def get_input():
    """Retrieve user input without any prompt."""
    return input()

def remove_spaces(s):
    """Remove all spaces from the provided string."""
    return ''.join(c for c in s if c != ' ')

def calculate_frequency_difference(str1, str2):
    """Calculate the frequency difference for characters from 'A' to 'z'."""
    frequency_diff = [0] * (ord('z') - ord('A') + 1)  # Initialize frequency list

    for char in range(ord('A'), ord('z') + 1):
        count1 = str1.count(chr(char))  # Count in first string
        count2 = str2.count(chr(char))  # Count in second string
        frequency_diff[char - ord('A')] = count1 - count2  # Store the frequency difference

    return frequency_diff

def check_negatives(frequency_diff):
    """Check for any negative values in the frequency list."""
    return any(value < 0 for value in frequency_diff)

def main():
    # Input two strings
    first_string = get_input()
    second_string = get_input()
    
    # Process the strings to remove spaces
    first_string_no_spaces = remove_spaces(first_string)
    second_string_no_spaces = remove_spaces(second_string)
    
    # Calculate frequency differences
    frequency_diff = calculate_frequency_difference(first_string_no_spaces, second_string_no_spaces)
    
    # Check frequency list for negative values
    if check_negatives(frequency_diff):
        print("NO")
    else:
        print("YES")

# Run the main function
if __name__ == "__main__":
    main()
