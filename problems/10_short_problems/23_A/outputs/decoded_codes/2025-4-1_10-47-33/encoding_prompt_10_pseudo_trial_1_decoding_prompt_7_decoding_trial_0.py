# Define the main function that encapsulates the overall process
def main():
    # Step 1: Read input and initialize variables
    line = input().strip()  # Read a line of input from standard input and remove any trailing spaces
    n = len(line)  # Get the length of the input string
    rv = 0  # This variable stores the result

    # Step 2: Iterate through lengths l from 0 to n-1
    for l in range(n):  # l will take values from 0 to n-1
        # Step 3: Check for substring presence
        for i in range(n):  # i will take values from 0 to n-1
            # Step 4: Check if the substring exists later in the string
            # Extract the substring line[i:i+l+1] (adding 1 to include the character at index i+l)
            substring = line[i:i+l+1]  # This gets the substring of length l+1
            # Check if the substring exists starting from index i+1
            if substring in line[i+1:]:
                rv = l  # Update rv with the current length l
                break  # Exit the inner loop as the substring is found
        else:
            continue  # Continue the outer loop if the break was not hit
        break  # If the inner loop was exited normally, break the outer loop as well

    # Step 5: Output the result
    print(rv)  # Display the final value of rv

# Ensure the main function runs if this script is executed
if __name__ == '__main__':
    main()
