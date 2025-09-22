def compare_strings():
    # Step 1: Read user input while ignoring spaces
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")
    
    # Step 2: Initialize a frequency list for character counts
    # We will use a dictionary to hold the frequency counts for each character
    frequency_differences = {}
    
    # Step 3: Count character frequencies for both strings
    for char in range(ord('A'), ord('z') + 1):
        char = chr(char)
        
        # Count occurrences of char in first_string and second_string
        count_in_first = first_string.count(char)
        count_in_second = second_string.count(char)
        
        # Calculate the difference in counts and store it in the dictionary
        frequency_differences[char] = count_in_first - count_in_second
    
    # Step 4: Check for non-negative counts
    negative_count = 0
    for diff in frequency_differences.values():
        if diff < 0:
            negative_count += 1
    
    # Step 5: Output result based on the count of negative frequencies
    if negative_count == 0:
        print("YES")  # String 1 has at least the same frequency of characters as String 2
    else:
        print("NO")   # String 1 does not match the character frequency of String 2

# Call the function to execute
compare_strings()
