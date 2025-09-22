# Function to determine if one string can be rearranged to match another
def can_rearrange_to_match():
    # Input collection
    first_string = input()
    second_string = input()
    
    # Remove spaces and create cleaned character lists
    cleaned_first_string = [char for char in first_string if char != ' ']
    cleaned_second_string = [char for char in second_string if char != ' ']
    
    # Initialize frequency count for each character (from ASCII 'A' to 'z')
    frequency_difference = [0] * (123)  # ASCII range from 'A' (65) to 'z' (122)

    # Calculate character frequencies
    for char in cleaned_first_string:
        frequency_difference[ord(char)] += 1  # Increment frequency for char in first string
    for char in cleaned_second_string:
        frequency_difference[ord(char)] -= 1  # Decrement frequency for char in second string

    # Check for negative counts
    negative_counts = [count for count in frequency_difference if count < 0]

    # Output result based on the negative counts
    if len(negative_counts) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
can_rearrange_to_match()
