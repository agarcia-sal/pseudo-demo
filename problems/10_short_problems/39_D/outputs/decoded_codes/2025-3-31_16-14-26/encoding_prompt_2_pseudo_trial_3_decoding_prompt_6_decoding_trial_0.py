def do_main():
    # Prompt user to input the first set of values and store it as a string
    first_input = input()
    # Prompt user to input the second set of values and store it as a string
    second_input = input()
    
    # Split the input strings into lists of individual string values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through each value for three iterations
    for index in range(3):
        # Convert the current string values to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Compare the two values
        if first_value != second_value:
            difference_count += 1  # Increase the difference count if they aren't equal
            
    # Check the final count of differences and output the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the function to run the program if this script is executed as the main program
if __name__ == "__main__":
    do_main()
