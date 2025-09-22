def check_if_strings_have_equal_character_counts():
    # INPUT: Read two lines of input strings
    first_string = input()
    second_string = input()
    
    # PROCESS: Remove spaces from both input strings
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")
    
    # Create a list to hold the frequency differences of characters
    frequency_differences = []
    
    # Determine the frequency of each character from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        # Count occurrences of character represented by ascii_value
        count_in_first = cleaned_first_string.count(chr(ascii_value))
        count_in_second = cleaned_second_string.count(chr(ascii_value))
        
        # Calculate the difference in counts
        difference = count_in_first - count_in_second
        
        # Store the difference in the frequency list
        frequency_differences.append(difference)
    
    # CHECK: Verify if all character frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Optionally, this line can be uncommented to run the function directly.
# check_if_strings_have_equal_character_counts()
