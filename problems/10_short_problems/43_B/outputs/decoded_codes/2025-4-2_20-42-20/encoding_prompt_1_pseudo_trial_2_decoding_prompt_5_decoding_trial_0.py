# Function to compare character frequencies between two strings
def compare_string_frequencies():
    # Read two input strings
    first_string = input()
    second_string = input()
    
    # Filter characters: remove spaces
    filtered_first = [char for char in first_string if char != ' ']
    filtered_second = [char for char in second_string if char != ' ']
    
    # Initialize frequency differences list for ASCII characters
    frequency_differences = [0] * (ord('z') + 1)  # Extend to cover all ASCII range needed
    
    # Count differences for each character in ASCII range
    for char in range(ord('A'), ord('z') + 1):
        count_first = filtered_first.count(chr(char))
        count_second = filtered_second.count(chr(char))
        frequency_differences[char] = count_first - count_second

    # Create a list of negative frequencies
    negative_frequencies = [diff for diff in frequency_differences if diff < 0]
    count_negative = len(negative_frequencies)
    
    # Output the result based on negative frequencies count
    if count_negative == 0:
        print("YES")
    else:
        print("NO")

# Example Usage
# compare_string_frequencies()  # Uncomment to run the function and test
