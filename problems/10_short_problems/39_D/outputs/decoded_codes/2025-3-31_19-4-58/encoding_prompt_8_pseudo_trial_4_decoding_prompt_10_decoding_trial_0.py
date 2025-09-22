def main():
    # Get input from the user
    first_input = input()
    second_input = input()

    # Split the inputs into lists of integers
    first_list = list(map(int, first_input.split()))
    second_list = list(map(int, second_input.split()))

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three items in both lists
    for index in range(3):
        # Compare the current values
        if first_list[index] != second_list[index]:
            # Increment the difference counter if values differ
            difference_count += 1 

    # Check how many values are different and decide outcome
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
