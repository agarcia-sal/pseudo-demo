# Function to compare character frequencies from two strings
def compare_character_frequencies():
    # Receive input from user
    first_string = input()
    second_string = input()

    # Process input to remove spaces
    processed_first_string = [char for char in first_string if char != ' ']
    processed_second_string = [char for char in second_string if char != ' ']

    # Initialize frequency count for characters 'A' to 'z'
    frequency_differences = [0] * (ord('z') + 1)

    # Calculate frequency differences
    for char in range(ord('A'), ord('z') + 1):
        count_in_first = processed_first_string.count(chr(char))
        count_in_second = processed_second_string.count(chr(char))
        
        # Store the difference in frequencies
        frequency_differences[char] = count_in_first - count_in_second

    # Determine result based on frequency differences
    if all(count >= 0 for count in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the function
compare_character_frequencies()
