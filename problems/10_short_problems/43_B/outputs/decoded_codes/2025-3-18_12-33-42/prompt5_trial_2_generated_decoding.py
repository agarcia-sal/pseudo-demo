# Function to compare the character frequencies of two strings
def compare_strings():
    # Step 1: Read two lines of text input
    first_string = input()
    second_string = input()
    
    # Step 2: Remove spaces from both strings
    cleaned_first_string = []
    cleaned_second_string = []
    
    for character in first_string:
        if character != ' ':
            cleaned_first_string.append(character)
    
    for character in second_string:
        if character != ' ':
            cleaned_second_string.append(character)

    # Step 3: Initialize frequency difference list
    freq_difference = []
    
    # Step 4: Calculate the frequency difference of characters
    for character in range(ord('A'), ord('z') + 1):
        char = chr(character)
        count_first = cleaned_first_string.count(char)
        count_second = cleaned_second_string.count(char)
        
        # Calculate frequency difference as count_first - count_second
        frequency_difference = count_first - count_second
        freq_difference.append(frequency_difference)
    
    # Step 5: Check if all frequency differences are non-negative
    has_negative_difference = False
    
    for difference in freq_difference:
        if difference < 0:
            has_negative_difference = True
            break

    # Step 6: Print the result
    if not has_negative_difference:
        print("YES")
    else:
        print("NO")

# Example of calling the function (commented out for clarity)
# compare_strings()
