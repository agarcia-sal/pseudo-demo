1. ACCEPT Input:
   - Read a line of text from standard input, removing any trailing newline character.

2. INITIALIZE Variables:
   - Set the total length of the input string as totalLength.
   - Create a variable longestRepeatedLength and initialize it to 0 to store the length of the longest repeated substring.

3. ITERATE Over Possible Substring Lengths:
   - FOR each potential substring length currentLength from 1 to totalLength - 1:
     - FOR each starting position startIndex from 0 to totalLength - currentLength:
       - Extract the substring from startIndex of length currentLength.
       - Check if this substring appears again in the input string starting from one position after startIndex.
       - IF this substring is found again:
         - Update longestRepeatedLength to currentLength.
         - BREAK the inner loop to stop searching for other substrings of this length.

4. OUTPUT Result:
   - PRINT longestRepeatedLength.


# Accept input from the user
input_string = input().strip()

# Initialize the total length of the input and the variable for the longest repeated substring length
total_length = len(input_string)
longest_repeated_length = 0

# Iterate over possible substring lengths
for current_length in range(1, total_length):  # Lengths from 1 to total_length - 1
    for start_index in range(total_length - current_length):  # Starting from 0 to total_length - current_length
        substring = input_string[start_index:start_index + current_length]  # Extract the substring
        
        # Check if the substring appears again in the input string
        if substring in input_string[start_index + 1:]:  # Check from one character after start_index
            longest_repeated_length = current_length  # Update longest repeated length
            break  # Stop searching for other substrings of this length

# Output the final result
print(longest_repeated_length)
