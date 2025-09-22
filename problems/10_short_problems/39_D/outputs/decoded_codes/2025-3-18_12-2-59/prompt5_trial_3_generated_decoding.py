def execute_main_logic():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of numbers
    first_set = first_line.split()
    second_set = second_line.split()

    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both sets
    for index in range(3):
        # Convert the current elements from both sets into integers
        first_number = int(first_set[index])
        second_number = int(second_set[index])
        
        # Check if the numbers are not equal
        if first_number != second_number:
            # Increment the difference counter
            difference_count += 1 
    
    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution by calling the main logic function
if __name__ == "__main__":
    execute_main_logic()
