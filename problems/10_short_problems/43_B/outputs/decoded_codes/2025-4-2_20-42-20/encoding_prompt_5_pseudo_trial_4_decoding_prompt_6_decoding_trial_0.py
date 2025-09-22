# Define the function to compare the character frequencies of two strings
def compare_strings():
    # Read user input, removing spaces by using replace method
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")
    
    # Initialize a frequency list for the characters from 'A' (65) to 'z' (122)
    frequency_differences = [0] * (123 - 65)  # 'A' to 'z' inclusive

    # Count frequencies for each character from 'A' to 'z'
    for char_code in range(65, 123):
        char = chr(char_code)  # Convert ASCII value to character
        
        # Count occurrences of the character in both strings
        count_in_first = first_string.count(char)
        count_in_second = second_string.count(char)

        # Calculate the difference and store it in the frequency list
        frequency_differences[char_code - 65] = count_in_first - count_in_second

    # Check for any negative counts
    has_negative_counts = any(count < 0 for count in frequency_differences)

    # Print the result based on the presence of negative counts
    if not has_negative_counts:
        print("YES")  # String 1 can match characters of String 2
    else:
        print("NO")   # String 1 cannot match characters of String 2

# Call the function to execute the comparison
compare_strings()
