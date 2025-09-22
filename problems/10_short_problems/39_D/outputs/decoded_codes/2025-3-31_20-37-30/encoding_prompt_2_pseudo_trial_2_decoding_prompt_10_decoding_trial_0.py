def do_main():
    # Get user input for the first and second lists
    first_input = input()
    second_input = input()

    # Split the inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Compare corresponding elements from both lists
    for index in range(3):  # Assuming we are only comparing 3 elements
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        if first_value != second_value:
            difference_count += 1

    # Determine and print the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# Execute the main function if the script is run directly
if __name__ == "__main__":
    do_main()


  1 2 3
  1 2 3
  

  1 2 3
  4 2 3
  

  1 2 3
  4 5 6
  