def main():
    # Prompt user for two inputs
    first_input = input()  # Get the first input from the user
    second_input = input()  # Get the second input from the user
    
    # Split the inputs into lists of values
    first_list = first_input.split()  # Split the first input into a list
    second_list = second_input.split()  # Split the second input into a list
    
    # Initialize a counter for differences
    difference_count = 0  # Initialize the difference counter
    
    # Iterate over the first three elements of both lists
    for index in range(3):  # Loop through index 0 to 2
        first_value = int(first_list[index])  # Convert first list value to integer
        second_value = int(second_list[index])  # Convert second list value to integer
        
        # Check if the current values are different
        if first_value != second_value:  # Compare the two values
            difference_count += 1  # Increment difference count if they are different
    
    # Decide the output based on the number of differences
    if difference_count < 3:  # Check if differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Start program execution
main()  # Call the main function
