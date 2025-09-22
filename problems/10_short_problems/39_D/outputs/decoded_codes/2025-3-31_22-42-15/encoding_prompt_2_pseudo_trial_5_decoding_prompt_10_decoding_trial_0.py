def do_main():
    # Read the first input line and store it as firstInput
    first_input = input()
    
    # Read the second input line and store it as secondInput
    second_input = input()
    
    # Split inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to keep track of differences
    mismatch_count = 0
    
    # Compare the values at each index (0 to 2)
    for index in range(3):
        # Convert the current index value to integer for both lists
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check for differences
        if first_value != second_value:
            mismatch_count += 1

    # Determine the result based on the mismatch count
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")


# Entry point of the program
if __name__ == "__main__":
    do_main()
