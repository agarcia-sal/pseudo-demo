def main():
    # Read two lines of input representing two sets of values
    first_input = input()  # Input for the first set of values
    second_input = input()  # Input for the second set of values
    
    # Split the input strings into lists of values
    first_values = first_input.split()  # List of values from the first input
    second_values = second_input.split()  # List of values from the second input
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Iterate through the first three values of both lists
    for index in range(3):  # Looping through the first three indices
        # Convert the current values from strings to integers
        value_a = int(first_values[index])  # Current value from the first list
        value_b = int(second_values[index])  # Current value from the second list
        
        # Compare the current values
        if value_a != value_b:  # Check for inequality
            # Increment the difference counter if they are different
            difference_count += 1
    
    # Check the number of differences
    if difference_count < 3:  # If there are fewer than three differences
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Invoke the main function when the script is executed
main()
