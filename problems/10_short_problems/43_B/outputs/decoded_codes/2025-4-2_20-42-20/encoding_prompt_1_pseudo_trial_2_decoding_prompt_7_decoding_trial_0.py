# Define a function to check if the second string contains enough characters from the first string.
def check_character_frequencies():
    # Input: Read two lines of input strings
    first_string = input()
    second_string = input()

    # Process the Strings: filter out spaces
    filtered_first = [char for char in first_string if char != ' ']
    filtered_second = [char for char in second_string if char != ' ']

    # Initialize Frequency Differences
    # Create a dictionary to count character frequencies
    frequency_differences = {chr(i): 0 for i in range(ord('A'), ord('z') + 1)}

    # Count frequency of each character in filtered_first
    for char in filtered_first:
        frequency_differences[char] += 1

    # Subtract frequency of each character in filtered_second
    for char in filtered_second:
        frequency_differences[char] -= 1

    # Check for Negative Frequencies
    negative_frequencies = [count for count in frequency_differences.values() if count < 0]

    # Output Result
    if len(negative_frequencies) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the logic
check_character_frequencies()
