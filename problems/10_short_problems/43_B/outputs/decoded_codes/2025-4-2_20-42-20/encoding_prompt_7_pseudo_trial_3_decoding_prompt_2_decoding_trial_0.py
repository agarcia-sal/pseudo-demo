def compare_string_frequencies():
    # Prompt user for input strings
    first_input_string = input()
    second_input_string = input()
    
    # Remove spaces from both input strings
    first_processed_string = [char for char in first_input_string if char != ' ']
    second_processed_string = [char for char in second_input_string if char != ' ']
    
    # Initialize a list to hold frequency differences
    frequency_differences = []
    
    # Calculate the frequency difference for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        first_string_count = first_processed_string.count(chr(character_code))
        second_string_count = second_processed_string.count(chr(character_code))
        
        # Calculate and add the difference in frequency to the list
        frequency_differences.append(first_string_count - second_string_count)
    
    # Check if there are any negative frequency differences
    negative_counts = [diff for diff in frequency_differences if diff < 0]
    
    # Print "YES" if no negative frequencies are found, otherwise print "NO"
    if len(negative_counts) == 0:
        print("YES")
    else:
        print("NO")

# Call the function
compare_string_frequencies()
