def compare_character_frequencies():
    # Get input strings from the user
    first_string = input()
    second_string = input()
    
    # Initialize a list to store cleaned strings (without spaces)
    cleaned_strings = []
    
    # Clean each string by removing spaces
    cleaned_strings.append(first_string.replace(" ", ""))
    cleaned_strings.append(second_string.replace(" ", ""))
    
    # Initialize a list to hold character frequency differences
    frequency_differences = []
    
    # Iterate over ASCII values from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):
        # Count occurrences in cleaned first string
        count_first = cleaned_strings[0].count(chr(char_code))
        # Count occurrences in cleaned second string
        count_second = cleaned_strings[1].count(chr(char_code))
        # Calculate frequency difference and store it
        frequency_differences.append(count_first - count_second)
    
    # Check if all frequency differences are non-negative
    if all(difference >= 0 for difference in frequency_differences):
        print("YES")  # Character frequencies match
    else:
        print("NO")   # Character frequencies do not match
