def check_string_formation():
    # Input Gathering
    first_string = input()
    second_string = input()
    
    # Process Input Strings
    first_list = list(first_string.replace(" ", ""))
    second_list = list(second_string.replace(" ", ""))
    
    # Initialize Frequency Count
    frequency_differences = []
    
    # Count Character Frequencies
    for char in range(ord('A'), ord('z') + 1):
        count_first = first_list.count(chr(char))
        count_second = second_list.count(chr(char))
        difference = count_first - count_second
        frequency_differences.append(difference)

    # Evaluate Frequencies
    negative_differences = [diff for diff in frequency_differences if diff < 0]
    
    # Output Result
    if len(negative_differences) == 0:
        print("YES")
    else:
        print("NO")

# To execute the function
check_string_formation()
