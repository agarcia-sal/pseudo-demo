def main():
    # Get two input strings representing numerical values
    first_set = input()
    second_set = input()

    # Split the input strings into lists of numerical strings
    first_numbers = first_set.split()
    second_numbers = second_set.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the range of three positions
    for position in range(3):
        # Convert the current positions' values from strings to integers
        value_from_first_set = int(first_numbers[position])
        value_from_second_set = int(second_numbers[position])

        # Check if the values from both sets differ
        if value_from_first_set != value_from_second_set:
            # Increment the difference counter
            difference_count += 1

    # Check the total differences and decide the output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
if __name__ == "__main__":
    main()


      1 2 3
      1 2 4
      

      1 2 3
      4 5 6
      

      10 20 30
      10 20 31
      