def check_character_frequency():
    # Prompt user for the first string input
    first_string = input()
    
    # Prompt user for the second string input
    second_string = input()
    
    # Create lists of characters from the input strings, excluding spaces
    first_filtered_list = [char for char in first_string if char != ' ']
    second_filtered_list = [char for char in second_string if char != ' ']

    # Initialize a list to hold frequency differences
    frequency_difference_list = []

    # Iterate through the ASCII values from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        current_char = chr(ascii_value)
        
        # Calculate the frequency difference of the current character
        frequency_difference = first_filtered_list.count(current_char) - second_filtered_list.count(current_char)
        
        # Append the frequency difference to the list
        frequency_difference_list.append(frequency_difference)

    # Check if there are any negative values in frequency_difference_list
    if all(diff >= 0 for diff in frequency_difference_list):
        print("YES")
    else:
        print("NO")

# Test cases for verification
# Example inputs: 
# first_string = "a b c"
# second_string = "a"
# Expected output: "YES"

# first_string = "hello"
# second_string = "world"
# Expected output: "NO"
