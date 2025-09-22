def main():
    # Read input values for two sets of data
    first_input = input()
    second_input = input()

    # Split the input values into lists
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert elements to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the numbers are different
        if first_number != second_number:
            # Increment the difference count
            difference_count += 1
            
    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
