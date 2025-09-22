def main():
    # Receive input from the user
    first_string = input()
    second_string = input()

    # Process input to remove spaces
    processed_first_string = [char for char in first_string if char != ' ']
    processed_second_string = [char for char in second_string if char != ' ']

    # Initialize frequency count for characters from 'A' to 'z'
    frequency_differences = [0] * (ord('z') - ord('A') + 1)

    # Calculate frequency differences
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)
        count_first = processed_first_string.count(char)
        count_second = processed_second_string.count(char)
        
        # Store the difference of counts
        frequency_differences[char_code - ord('A')] = count_first - count_second

    # Determine result based on frequency differences
    if all(count >= 0 for count in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the main function to execute the code
main()
