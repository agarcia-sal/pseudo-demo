def main():
    # Step 1: Read a line of input from the standard input
    line = input()
    
    # Step 2: Remove the last character from the input line (typically a newline)
    line = line[:-1]  # Assuming the last character is a newline
    
    # Step 3: Determine the length of the line
    n = len(line)
    
    # Step 4: Initialize a variable to store the result
    result_length = 0
    
    # Step 5: Iterate through possible substring lengths from 0 to n-1
    for length in range(n):  # lengths from 0 to n-1
        # Step 6: Iterate through each character in the line
        for start_index in range(n):
            # Step 7: Extract the substring of the current length
            if start_index + length <= n:
                substring = line[start_index:start_index + length]
                # Check if this substring can be found elsewhere in the line after start_index
                found_index = line.find(substring, start_index + 1)
                
                if found_index != -1:  # IF found
                    # Step 8: Update result_length to the current length
                    result_length = length
                    # Step 9: Exit the inner loop since a match is found
                    break
        else:
            continue  # Continue the outer loop if inner loop did not break
        break  # Break if we found a matching substring, exiting the outer loop
    
    # Step 10: Output the result
    print(result_length)

if __name__ == "__main__":
    main()
