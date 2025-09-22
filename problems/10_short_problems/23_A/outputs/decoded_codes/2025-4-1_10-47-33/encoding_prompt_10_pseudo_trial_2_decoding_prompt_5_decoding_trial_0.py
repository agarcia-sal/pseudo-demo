# Function to find the largest length of repeated substrings in a given string
def find_largest_repeated_substring():
    # Read input and remove the last character
    line = input()[:-1]  
   
    # Determine the length of the input string
    n = len(line)  
    rv = 0  # This will hold the result for the largest length found

    # Loop through possible substring lengths from 0 to n-1
    for l in range(n):
        # Loop through each starting index for the substring
        for i in range(n):
            # Check if the substring from index i with length l appears again
            if line[i:i + l] in line[i + 1:]:
                rv = l  # Update rv if we find a repeated substring
                break  # Exit the inner loop as we found a match

    # Output the largest length of repeated substring found
    print(rv)

# Example of how to call the function (uncomment to test):
# find_largest_repeated_substring() 
