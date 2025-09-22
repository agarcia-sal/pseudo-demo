# Function to check the frequency difference of characters in two strings
def frequency_difference():
    # Input two strings from the user
    first_string = input()
    second_string = input()

    # Process strings to remove spaces
    first_string = ''.join(first_string.split())
    second_string = ''.join(second_string.split())

    # Initialize frequency list for characters from 'A' to 'z'
    frequency_diff = [0] * (ord('z') - ord('A') + 1)

    # Calculate frequency difference for each character from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)
        count_first = first_string.count(char)  # Count in first string
        count_second = second_string.count(char)  # Count in second string
        frequency_diff[char_code - ord('A')] = count_first - count_second  # Store difference

    # Count how many values in frequency list are less than zero
    negative_count = sum(1 for freq in frequency_diff if freq < 0)

    # Output result based on the count of negative values
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
frequency_difference()
