def main():
    # Accept input for the first set of values
    first_set = input()
    
    # Accept input for the second set of values
    second_set = input()

    # Split the input strings into lists of individual numbers
    first_values = first_set.split()
    second_values = second_set.split()

    # Initialize a counter for the number of differences
    difference_count = 0 

    # Loop through each position to compare the values
    for index in range(3):
        # Convert the current values from string to integer
        value_from_first_set = int(first_values[index])
        value_from_second_set = int(second_values[index])

        # Check if the values at the current index are different
        if value_from_first_set != value_from_second_set:
            # Increase the difference counter by one
            difference_count += 1 

    # Determine if the number of differences is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()


   1 2 3
   1 2 4
   

   5 6 7
   8 9 10
   

   10 20 30
   10 20 30
   

   1 2 3
   3 2 1
   

   0 0 0
   1 1 1
   