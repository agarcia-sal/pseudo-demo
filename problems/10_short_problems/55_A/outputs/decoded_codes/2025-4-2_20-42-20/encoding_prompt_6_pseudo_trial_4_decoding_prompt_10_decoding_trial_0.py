def main():
    # Accept an integer input representing the size of the array
    array_size = int(input())  # Read and convert input to an integer

    # Initialize a boolean array of size 'array_size' with all values set to True
    boolean_array = [True] * array_size

    # Initialize the index variable for the boolean array and a counter variable starting from 1
    index = 0
    counter = 1

    # Loop for a maximum of 500000 iterations
    for _ in range(500000):
        # If the current position in the boolean array is still True
        if boolean_array[index]:
            # Set the current position in the boolean array to False
            boolean_array[index] = False
        
        # Move to the next number by incrementing the counter
        counter += 1
        
        # Calculate the new index in a circular manner
        index = (index + counter) % array_size

    # Create a new list of elements from the boolean array that are still True
    true_values = [value for value in boolean_array if value]

    # Check if there are any True values left in the list
    if len(true_values) == 0:
        # If there are no True values, print "YES"
        print("YES")
    else:
        # If there are any True values, print "NO"
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
