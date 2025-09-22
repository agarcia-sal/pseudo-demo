def main():
    # Read two lines of input representing two sets of data
    first_set = input()
    second_set = input()
    
    # Split the input data into individual components
    first_components = first_set.split()
    second_components = second_set.split()
    
    # Initialize a counter to track differences
    difference_count = 0
    
    # Iterate through the first three components (assuming valid input)
    for index in range(3):
        # Convert the components from strings to integers
        first_value = int(first_components[index])
        second_value = int(second_components[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter if they are different
            difference_count += 1
    
    # Evaluate the total number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main program execution starts here
main()
