def check_character_frequency_difference():
    # Initialize two empty lists to hold the cleaned input strings
    s1 = []
    s2 = []
    
    # Read and clean the first input string
    input_string1 = input()
    cleaned_string1 = input_string1.replace(" ", "")  # Remove spaces
    s1.append(cleaned_string1)  # Store the cleaned string in s1
    
    # Read and clean the second input string
    input_string2 = input()
    cleaned_string2 = input_string2.replace(" ", "")  # Remove spaces
    s2.append(cleaned_string2)  # Store the cleaned string in s2
    
    # Initialize a list to hold the frequency differences
    freqs = []
    
    # For each character code from 'A' to 'z' (ASCII range)
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)  # Convert the ASCII code to the character
        count_s1 = cleaned_string1.count(char)  # Count occurrences in s1
        count_s2 = cleaned_string2.count(char)  # Count occurrences in s2
        # Calculate the difference and store it in freqs
        freqs.append(count_s1 - count_s2)
    
    # Check if there are any negative values in the freqs list
    if all(freq >= 0 for freq in freqs):
        print("YES")  # Output "YES" if there are no negative values
    else:
        print("NO")  # Output "NO" otherwise

# Call the function to execute
check_character_frequency_difference()
