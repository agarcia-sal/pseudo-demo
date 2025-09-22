def main_procedure():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a variable to count differences
    difference_count = 0
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current element from each list to an integer
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])
        
        # Check if the two values are different
        if value_from_first_list != value_from_second_list:
            # Increment the difference counter
            difference_count += 1

    # Check the total number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main_procedure()
