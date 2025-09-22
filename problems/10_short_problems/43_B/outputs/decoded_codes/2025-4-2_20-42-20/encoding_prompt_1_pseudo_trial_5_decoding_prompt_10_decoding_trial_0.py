def read_input_strings():
    """Reads two input strings from the user."""
    string1 = input()
    string2 = input()
    return string1, string2

def clean_string(input_string):
    """Removes spaces from the input string and returns a list of characters."""
    return [char for char in input_string if char != ' ']

def calculate_frequency_differences(cleaned_string1, cleaned_string2):
    """Calculates frequency differences between characters in two cleaned strings."""
    frequency_differences = []

    for char_code in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
        char = chr(char_code)
        count1 = cleaned_string1.count(char)
        count2 = cleaned_string2.count(char)
        frequency_differences.append(count1 - count2)

    return frequency_differences

def check_frequency_differences(frequency_differences):
    """Checks how many negative values exist in the frequency differences list."""
    negative_count = sum(1 for diff in frequency_differences if diff < 0)
    return negative_count == 0

def main():
    """Main function to execute the program logic."""
    string1, string2 = read_input_strings()
    
    cleaned_string1 = clean_string(string1)
    cleaned_string2 = clean_string(string2)
    
    frequency_differences = calculate_frequency_differences(cleaned_string1, cleaned_string2)
    
    if check_frequency_differences(frequency_differences):
        print("YES")
    else:
        print("NO")

# Invoke the main function when the script is run
if __name__ == "__main__":
    main()
