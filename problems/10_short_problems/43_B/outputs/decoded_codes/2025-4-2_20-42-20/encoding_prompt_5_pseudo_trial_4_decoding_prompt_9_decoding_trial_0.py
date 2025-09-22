def compare_strings():
    # Read user input for both strings
    first_string = input()
    second_string = input()
    
    # Remove spaces from both strings
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    
    # Initialize frequency differences for characters from 'A' to 'z'
    frequency_differences = [0] * (123 - 65)  # From ASCII 'A' (65) to 'z' (122)
    
    # Count character frequencies for each character
    for ascii_value in range(65, 123):  # 65 to 122 is range for 'A' to 'z'
        char_in_first = first_string.count(chr(ascii_value))
        char_in_second = second_string.count(chr(ascii_value))
        
        # Calculate the difference in frequency and store it
        frequency_differences[ascii_value - 65] = char_in_first - char_in_second
    
    # Check for non-negative counts in frequency_differences
    if all(count >= 0 for count in frequency_differences):
        print("YES")  # String 1 can match characters of string 2
    else:
        print("NO")   # String 1 cannot match characters of string 2
