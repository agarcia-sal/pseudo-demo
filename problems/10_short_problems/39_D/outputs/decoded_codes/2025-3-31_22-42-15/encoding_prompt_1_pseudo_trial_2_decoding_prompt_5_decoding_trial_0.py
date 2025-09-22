def doMain():
    # Get input values from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of individual string values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for the differences
    difference_count = 0
    
    # Iterate through index values 0 to 2 (inclusive)
    for index in range(3):
        # Convert string values to integers
        value_a = int(first_values[index])
        value_b = int(second_values[index])
        
        # Check if the values are different
        if value_a != value_b:
            # Increase the difference counter
            difference_count += 1
    
    # Decide output based on the difference count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    doMain()
