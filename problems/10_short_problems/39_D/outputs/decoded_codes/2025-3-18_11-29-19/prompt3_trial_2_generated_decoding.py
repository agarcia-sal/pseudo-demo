def main():
    # Get two sets of inputs from the user
    first_time_string = input()
    second_time_string = input()

    # Split the input strings into lists of strings
    first_time_list = first_time_string.split()
    second_time_list = second_time_string.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers
        first_time_value = int(first_time_list[index])
        second_time_value = int(second_time_list[index])

        # Compare the two values and count differences
        if first_time_value != second_time_value:
            difference_count += 1 

    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else: 
        print("NO")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
