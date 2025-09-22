def main():
    # Read two lines of input, representing two sets of values
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string values to integers for comparison
        value_from_first = int(first_values[index])
        value_from_second = int(second_values[index])
        
        # Check if the values are different
        if value_from_first != value_from_second:
            # Increment the difference counter
            difference_count += 1
            
    # Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()
