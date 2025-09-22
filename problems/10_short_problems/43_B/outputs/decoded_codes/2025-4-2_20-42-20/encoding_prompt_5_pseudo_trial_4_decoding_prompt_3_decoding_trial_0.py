def compare_strings():
    # Prompt user for input and remove spaces
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")
    
    # Initialize a frequency list for character counts (from A to z)
    # ASCII values: A=65, z=122, thus we need (122 - 65 + 1) = 58 slots
    frequency_differences = [0] * (123 - 65)  # There's 58 characters from 'A' to 'z'
    
    # Count character frequencies for both strings
    for char in range(65, 123):  # From ASCII 'A' (65) to 'z' (122)
        char_count_first = first_string.count(chr(char))  # Count in first string
        char_count_second = second_string.count(chr(char))  # Count in second string
        
        # Calculate the difference and store it in the frequency list
        frequency_differences[char - 65] = char_count_first - char_count_second
    
    # Check for non-negative counts
    negative_count = sum(1 for diff in frequency_differences if diff < 0)
    
    # Output result based on the count of negative frequencies
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# The function will run and expect input from users
compare_strings()
