def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()

    # Split the input lines into separate values
    first_values = first_line.split()
    second_values = second_line.split()

    # Initialize a variable to count differences
    difference_count = 0 
    
    # Compare corresponding values from both lists
    for index in range(3):
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check for inequality between the two values
        if first_value != second_value:
            difference_count += 1 

    # Determine the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the main function
if __name__ == "__main__":
    main()


1 2 3
1 2 4


1 2 3
4 5 6


0 0 0
0 0 0
