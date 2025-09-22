# Function to find the length of the longest substring that appears more than once
def find_longest_repeating_substring():
    # Step 1: Read input and initialize variables
    line = input()  # Read a line of input
    line = line[:-1]  # Remove the last character from the line
    n = len(line)  # Get the length of the line
    result_length = 0  # Variable to store the length of the longest repeating substring

    # Step 2: Iterate through lengths l from 0 to n-1
    for length in range(n):
        # Step 3: Check for substring presence
        for i in range(n):
            # Step 4: Check if the substring exists later in the string
            substring = line[i:i+length]  # Extract the substring
            if substring in line[i+1:]:  # Check if substring exists later in the string
                result_length = length  # Update result_length with the current length
                break  # Exit the inner loop as the substring is found
        if result_length != 0:  # If a repeating substring was found, break out of the outer loop
            break

    # Step 5: Output the result
    print(result_length)  # Display the final value of result_length

# Call the function to execute
find_longest_repeating_substring()
