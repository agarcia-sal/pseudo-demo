def check_character_frequencies():
    # Step 1: Receive Input and Clean Strings
    cleaned_string1 = input().replace(" ", "")
    cleaned_string2 = input().replace(" ", "")
    
    # Step 2: Initialize Frequency List
    frequency_differences = []
    
    # Step 3: Calculate Frequency Differences
    for ascii_value in range(65, 123):  # ASCII values from 'A' to 'z'
        char = chr(ascii_value)
        count_in_string1 = cleaned_string1.count(char)
        count_in_string2 = cleaned_string2.count(char)
        
        # Calculate the difference and store it
        frequency_difference = count_in_string1 - count_in_string2
        frequency_differences.append(frequency_difference)
    
    # Step 4: Check for Negative Differences
    negative_differences = [diff for diff in frequency_differences if diff < 0]
    
    # Output result based on the existence of negative differences
    if not negative_differences:  # means there are no negative differences
        print("YES")
    else:
        print("NO")

# Call the function to execute the logic
check_character_frequencies()
