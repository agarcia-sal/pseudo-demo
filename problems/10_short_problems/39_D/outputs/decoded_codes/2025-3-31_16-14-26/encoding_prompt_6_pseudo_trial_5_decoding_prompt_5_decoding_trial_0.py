def main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into separate values
    first_values = first_line.split()
    second_values = second_line.split()

    # Initialize a counter to track differences
    difference_count = 0 

    # Iterate through the first three values of both inputs
    for index in range(3):
        # Convert the current values from strings to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increase the difference counter
            difference_count += 1 

    # If there are fewer than three differences, print "YES", otherwise print "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the main function if this script is executed
if __name__ == "__main__":
    main()
