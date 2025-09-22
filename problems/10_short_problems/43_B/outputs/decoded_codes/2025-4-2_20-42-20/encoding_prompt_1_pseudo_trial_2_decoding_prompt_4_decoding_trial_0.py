def compare_string_frequencies():
    # Step 1: Read two lines of input strings
    first_string = input().strip()
    second_string = input().strip()
    
    # Step 2: Process the Strings
    filtered_first = [char for char in first_string if char != ' ']
    filtered_second = [char for char in second_string if char != ' ']
    
    # Step 3: Initialize Frequency Differences
    frequency_differences = []
    for char in range(ord('A'), ord('z') + 1):
        char_count_first = filtered_first.count(chr(char))
        char_count_second = filtered_second.count(chr(char))
        frequency_differences.append(char_count_first - char_count_second)
    
    # Step 4: Check for Negative Frequencies
    negative_frequencies = [count for count in frequency_differences if count < 0]
    
    # Step 5: Output Result
    if len(negative_frequencies) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
compare_string_frequencies()
