def main():
    # Prompt the user for input
    first_input = input()
    second_input = input()

    # Split the input into separate components
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a variable to count differences
    difference_count = 0

    # Compare the components from both input lists
    for i in range(3):
        first_value = int(first_list[i])
        second_value = int(second_list[i])
        
        if first_value != second_value:
            difference_count += 1

    # Determine the output based on differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
if __name__ == "__main__":
    main()
