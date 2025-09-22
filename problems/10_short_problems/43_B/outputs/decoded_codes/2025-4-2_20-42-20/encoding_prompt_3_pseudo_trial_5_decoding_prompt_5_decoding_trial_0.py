# Function to compare character frequencies in two input lines
def compare_character_frequencies():
    # Step 1: Read two lines of input
    first_line = input()
    second_line = input()
    
    # Step 2: Remove spaces from both lines
    cleaned_first_line = list(first_line.replace(" ", ""))
    cleaned_second_line = list(second_line.replace(" ", ""))
    
    # Step 3: Initialize frequency difference list
    frequency_differences = []
    
    # Step 4: Calculate the character frequency differences
    for ascii_value in range(ord('A'), ord('z') + 1):
        character = chr(ascii_value)
        count_in_first_line = cleaned_first_line.count(character)
        count_in_second_line = cleaned_second_line.count(character)
        difference = count_in_first_line - count_in_second_line
        frequency_differences.append(difference)
    
    # Step 5: Check if all frequency differences are non-negative
    has_negative_difference = False
    
    for value in frequency_differences:
        if value < 0:
            has_negative_difference = True
            break
    
    # Step 6: Print result based on the frequency differences
    if not has_negative_difference:
        print("YES")
    else:
        print("NO")

# Example test cases can be added as comments for future reference
# compare_character_frequencies() should be tested with various inputs
# For example:
# Input:
# "A B C"
# "A B"
# Output: "YES"
