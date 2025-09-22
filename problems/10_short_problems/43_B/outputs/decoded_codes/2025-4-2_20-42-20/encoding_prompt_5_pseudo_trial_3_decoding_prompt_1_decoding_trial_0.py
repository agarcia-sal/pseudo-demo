def CompareCharacterFrequencies():
    # Input: Get the first string and the second string from the user
    first_string = input()
    second_string = input()
    
    # Process: Initialize a list for the cleaned strings
    cleaned_strings = []
    
    # For each string input, remove spaces and store the cleaned version
    cleaned_strings.append(first_string.replace(" ", ""))
    cleaned_strings.append(second_string.replace(" ", ""))
    
    # Initialize a list for frequency differences
    frequency_differences = [0] * (ord('z') - ord('A') + 1)  # List to hold frequency differences

    # For each character code from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        char_count_first = cleaned_strings[0].count(chr(char_code))
        char_count_second = cleaned_strings[1].count(chr(char_code))
        
        # Calculate the difference in counts
        frequency_difference = char_count_first - char_count_second
        
        # Store this difference
        frequency_differences[char_code - ord('A')] = frequency_difference
    
    # Check if all values in frequencyDifferences are >= 0
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")  # Outputs that the character frequencies match
    else:
        print("NO")  # Outputs that there is a mismatch in character frequencies
