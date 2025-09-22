def doMain():
    # Accept user input for two sets of three numerical values
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for the differences
    difference_count = 0
    
    # Compare each corresponding value in the two lists
    for x in range(3):
        first_value = int(first_values[x])  # Convert to integer
        second_value = int(second_values[x])  # Convert to integer
        
        # Increase the counter if the values differ
        if first_value != second_value:
            difference_count += 1
    
    # Output "YES" if fewer than 3 positions differ, otherwise "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is the main program
if __name__ == "__main__":
    doMain()
