def string_frequency_difference():
    # Step 1: Input two strings
    first_string = input()
    second_string = input()
    
    # Step 2: Process the strings to remove spaces
    first_string = ''.join(first_string.split())
    second_string = ''.join(second_string.split())
    
    # Step 3: Initialize a frequency list
    frequency_list = [0] * (ord('z') - ord('A') + 1)  # Size to accommodate 'A' to 'z' (total 58 characters)
    
    # Step 4: Calculate the frequency difference
    for char in range(ord('A'), ord('z') + 1):  # Iterate through ASCII values of 'A' to 'z'
        count_first = first_string.count(chr(char))  # Count in the first string
        count_second = second_string.count(chr(char))  # Count in the second string
        frequency_list[char - ord('A')] = count_first - count_second  # Store difference in frequency list
    
    # Step 5: Check the frequency list for negative values
    negative_count = sum(1 for freq in frequency_list if freq < 0)  # Count how many negatives

    # Step 6: Output the result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Test the function
string_frequency_difference()
