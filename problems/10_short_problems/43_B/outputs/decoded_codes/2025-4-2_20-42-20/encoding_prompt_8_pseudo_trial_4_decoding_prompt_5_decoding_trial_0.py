# Function to compare character frequencies of two input strings
def compare_character_frequencies():
    # Initialize lists to store input strings after removing spaces
    first_input = input().replace(" ", "")
    second_input = input().replace(" ", "")
    
    # Create a list to hold the difference in character counts
    character_frequency_difference = [0] * 256  # ASCII range
    
    # Count character frequencies for both strings
    for char in first_input:
        character_frequency_difference[ord(char)] += 1  # Increment count for first input
    
    for char in second_input:
        character_frequency_difference[ord(char)] -= 1  # Decrement count for second input
    
    # Check if first_input has equal or more of every character compared to second_input
    for difference in character_frequency_difference:
        if difference < 0:  # If there is a negative difference
            print("NO")
            return  # Exit if any character is lacking
    
    print("YES")  # If all characters are sufficient

# Example test cases:
# compare_character_frequencies()  # Uncomment to run and test with inputs

