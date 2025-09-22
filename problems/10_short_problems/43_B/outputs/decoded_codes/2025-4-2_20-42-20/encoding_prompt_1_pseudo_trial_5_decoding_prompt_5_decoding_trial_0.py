# Function to compare two strings for character frequency differences
def compare_string_frequencies():
    # Step 1: Read Input
    string1 = input()
    string2 = input()
    
    # Step 2: Remove spaces and create cleaned strings
    cleaned_string1 = [char for char in string1 if char != ' ']
    cleaned_string2 = [char for char in string2 if char != ' ']
    
    # Step 3: Initialize Frequency Difference List
    frequency_differences = []
    
    # Step 4: Calculate Frequency Differences
    for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
        char = chr(ascii_value)
        count_in_string1 = cleaned_string1.count(char)
        count_in_string2 = cleaned_string2.count(char)
        frequency_difference = count_in_string1 - count_in_string2
        frequency_differences.append(frequency_difference)
    
    # Step 5: Check Frequency Differences
    negative_count = sum(1 for diff in frequency_differences if diff < 0)
    
    # Step 6: Output Result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Testing the function could be done in the following way:
# compare_string_frequencies()  # You can manually input strings when prompted
