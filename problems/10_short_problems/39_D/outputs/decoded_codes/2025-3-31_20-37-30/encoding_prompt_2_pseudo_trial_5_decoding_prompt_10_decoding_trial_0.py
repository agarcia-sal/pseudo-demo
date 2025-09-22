def main():
    # Read input from the user
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize the difference count
    difference_count = 0
    
    # Iterate over the first three indices
    for index in range(3):
        # Convert elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Count the differences
        if first_value != second_value:
            difference_count += 1
            
    # Determine output based on the difference count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program runs
if __name__ == "__main__":
    main()
