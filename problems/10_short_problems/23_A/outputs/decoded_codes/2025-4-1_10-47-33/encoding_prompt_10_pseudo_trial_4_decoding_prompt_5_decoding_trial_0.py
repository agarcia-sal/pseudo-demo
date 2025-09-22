# Function to find the length of the longest repeating substring
def longest_repeating_substring():
    # Read a line of input from the user
    line = input().strip()  # Read input and remove the newline character
    n = len(line)  # Determine the length of the input line
    max_length = 0  # Initialize the result variable to hold the maximum length of the repeating substring

    # Loop through all possible lengths of substrings from 0 to n-1
    for l in range(n):  # l represents the length of the substring
        # Loop through the starting index of the substring
        for i in range(n):  # i represents the starting index of the substring
            # Check if the substring from index i to i+l exists later in the string
            substring = line[i:i+l+1]  # Extract the substring from i to i+l
            if line.find(substring, i + 1) != -1:  # Look for substring after the current index
                max_length = l + 1  # Update max_length to current length l+1
                break  # Exit the inner loop once a match is found
    
    # Print the result variable indicating the length of the substring found
    print(max_length)

# Example usage (this part will generally not be included in a submitted solution)
# longest_repeating_substring()
