def main():
    # Step 1: Get input
    first_input = input()
    second_input = input()

    # Step 2: Split the inputs into lists of strings
    first_list = first_input.split()  # Splitting using spaces
    second_list = second_input.split()  # Splitting using spaces

    # Initialize a counter to track differences
    difference_count = 0

    # Step 3: Compare corresponding elements of the two lists
    for index in range(3):  # Iterate from 0 to 2
        # Convert string elements to integers
        value_from_first_list = int(first_list[index])
        value_from_second_list = int(second_list[index])
        
        # Check if the values are different
        if value_from_first_list != value_from_second_list:
            difference_count += 1  # Increment the counter if they are different

    # Step 4: Check the number of differences
    if difference_count < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")   # Print NO otherwise

# Invoke the main function when running the program
main()
