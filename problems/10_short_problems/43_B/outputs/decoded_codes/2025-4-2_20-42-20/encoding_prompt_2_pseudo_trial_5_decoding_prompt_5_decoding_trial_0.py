# Function to compare character frequencies of two input strings
def compare_character_frequencies():
    # Get input from the user
    first_string = input()
    second_string = input()
    
    # Process input strings by removing spaces
    processed_first_string = []
    processed_second_string = []
    
    # Add non-space characters from the first string to the list
    for char in first_string:
        if char != ' ':
            processed_first_string.append(char)
    
    # Add non-space characters from the second string to the list
    for char in second_string:
        if char != ' ':
            processed_second_string.append(char)
    
    # Initialize a list to store the frequency differences
    frequency_differences = []
    
    # Calculate frequency differences for ASCII values from 'A' to 'z'
    for ascii_code in range(ord('A'), ord('z') + 1):
        count_first = processed_first_string.count(chr(ascii_code))
        count_second = processed_second_string.count(chr(ascii_code))
        frequency_difference = count_first - count_second
        frequency_differences.append(frequency_difference)
    
    # Check if there are any negative values in frequency differences
    if any(diff < 0 for diff in frequency_differences):
        print("NO")
    else:
        print("YES")

# Call the function to execute the character frequency comparison
compare_character_frequencies()
