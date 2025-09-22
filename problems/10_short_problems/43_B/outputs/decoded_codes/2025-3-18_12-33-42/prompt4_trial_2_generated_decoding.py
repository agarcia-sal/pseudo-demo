def get_string_without_spaces():
    return input().replace(" ", "")

def count_character_frequency(s, char):
    return s.count(char)

def check_frequency_differences(s1, s2):
    frequency_differences = []
    
    for ascii_value in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
        character = chr(ascii_value)  # Convert ASCII value to character
        frequency_in_s1 = count_character_frequency(s1, character)
        frequency_in_s2 = count_character_frequency(s2, character)
        
        # Calculate the difference and store it in the list
        difference = frequency_in_s1 - frequency_in_s2
        frequency_differences.append(difference)

    # Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Main execution starts here
s1 = get_string_without_spaces()  # Get first string from user input
s2 = get_string_without_spaces()  # Get second string from user input
check_frequency_differences(s1, s2)  # Check and print results
