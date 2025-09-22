def main():
    # Step 1: Read a line of input from the standard input
    line = input()
    
    # Step 2: Remove the last character from the input line (typically a newline)
    line = line[:-1]  # Removing the last character
    
    # Step 3: Determine the length of the line
    n = len(line)
    
    # Step 4: Initialize a variable to store the result
    rv = 0
    
    # Step 5: Iterate through possible substring lengths from 0 to n-1
    for l in range(n):
        # Step 6: Iterate through each character in the line
        for i in range(n):
            # Step 7: Extract the substring of length l starting at index i
            substring = line[i:i + l]
            
            # Ensure the substring is valid and check for duplicates
            if substring and line.find(substring, i + 1) != -1:
                # Step 8: Update rv to the current length l
                rv = l
                
                # Step 9: Exit the inner loop since a match is found
                break
    
    # Step 10: Output the result
    print(rv)

# Call the main function to execute the code
if __name__ == "__main__":
    main()
