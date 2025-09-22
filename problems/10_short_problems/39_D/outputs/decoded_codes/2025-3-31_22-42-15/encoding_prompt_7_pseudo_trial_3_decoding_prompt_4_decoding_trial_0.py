def main():
    # Take inputs for two sets of values
    first_set = input()
    second_set = input()

    # Split the input strings into individual elements
    first_values = first_set.split()
    second_values = second_set.split()

    # Initialize a counter for differences
    difference_count = 0

    # Iterate over the first three elements of both sets
    for index in range(3):
        # Convert current elements from string to integer
        a = int(first_values[index])
        b = int(second_values[index])

        # Check if elements at the current index are different
        if a != b:
            difference_count += 1

    # Determine if the difference count is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when running the script
if __name__ == "__main__":
    main()


   1 2 3
   1 2 3
   

   1 2 3
   4 5 6
   

   2 3 5
   2 1 5
   