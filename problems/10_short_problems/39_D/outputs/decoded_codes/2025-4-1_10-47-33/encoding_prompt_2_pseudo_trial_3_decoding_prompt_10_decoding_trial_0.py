def main():
    # Prompting user for input
    first_input = input()
    second_input = input()
    
    # Processing the inputs: splitting into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter to track differences
    difference_count = 0

    # Compare elements in both lists
    for index in range(3):
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        if first_value != second_value:
            difference_count += 1

    # Determine the result based on difference count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
