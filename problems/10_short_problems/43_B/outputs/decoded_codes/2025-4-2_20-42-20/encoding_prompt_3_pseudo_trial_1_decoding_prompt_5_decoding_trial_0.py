# Function to compare two strings based on character frequencies
def compare_string_frequencies():
    # Read two inputs from the user
    first_input = input()
    second_input = input()
    
    # Remove spaces from both strings
    cleaned_first_input = first_input.replace(" ", "")
    cleaned_second_input = second_input.replace(" ", "")
    
    # Initialize a list to track character count differences
    frequency_differences = []
    
    # Iterate through ASCII values of 'A' to 'z' 
    for character_code in range(ord('A'), ord('z') + 1):
        # Count occurrences of the character in each cleaned input
        count_in_first_input = cleaned_first_input.count(chr(character_code))
        count_in_second_input = cleaned_second_input.count(chr(character_code))
        
        # Calculate the difference in counts and add to the frequency_differences list
        frequency_differences.append(count_in_first_input - count_in_second_input)
    
    # Count how many items in frequency_differences are negative
    non_negative_count = sum(1 for difference in frequency_differences if difference < 0)
    
    # Output the result based on whether any negative counts were found
    if non_negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the comparison
compare_string_frequencies()
