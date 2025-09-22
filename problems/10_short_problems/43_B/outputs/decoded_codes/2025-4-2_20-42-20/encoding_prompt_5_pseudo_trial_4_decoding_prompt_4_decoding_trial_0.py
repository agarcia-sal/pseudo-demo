def compare_strings():
    # Read user inputs, ignoring spaces
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")
    
    # Initialize frequency differences list
    frequency_differences = [0] * (ord('z') - ord('A') + 1)

    # Calculate frequency counts for each character
    for char in range(ord('A'), ord('z') + 1):
        count_first = first_string.count(chr(char))
        count_second = second_string.count(chr(char))
        # Store the difference of frequencies
        frequency_differences[char - ord('A')] = count_first - count_second

    # Check for negative frequencies
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the function to execute
compare_strings()
