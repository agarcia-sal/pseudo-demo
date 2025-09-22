def compare_character_frequencies():
    # Get inputs from the user
    first_string = input()
    second_string = input()
    
    # Initialize a list to store cleaned strings without spaces
    cleaned_strings = []
    
    # Clean the strings by removing spaces
    for string in [first_string, second_string]:
        cleaned_string = string.replace(" ", "")
        cleaned_strings.append(cleaned_string)
    
    # Prepare a list to store differences in character counts
    frequency_differences = []
    
    # Iterate over character ASCII codes from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)
        
        # Count occurrences in both cleaned strings
        count_first = cleaned_strings[0].count(char)
        count_second = cleaned_strings[1].count(char)
        
        # Calculate the difference and store it
        difference = count_first - count_second
        frequency_differences.append(difference)
    
    # Check if all values in frequency_differences are greater than or equal to zero
    if all(difference >= 0 for difference in frequency_differences):
        print("YES")  # Frequencies match
    else:
        print("NO")   # Frequencies do not match

# Call the function to execute
compare_character_frequencies()
