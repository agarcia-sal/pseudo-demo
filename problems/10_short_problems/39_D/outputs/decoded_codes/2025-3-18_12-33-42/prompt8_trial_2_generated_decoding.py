def main():
    # Read two lines of input, each containing three numbers
    string1 = input()
    string2 = input()
    
    # Split the input strings into lists of numbers
    numbers1 = string1.split()  # Split the first input by spaces
    numbers2 = string2.split()  # Split the second input by spaces
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers for comparison
        number1 = int(numbers1[index])  # Convert first list value to integer
        number2 = int(numbers2[index])  # Convert second list value to integer
        
        # Compare the two numbers
        if number1 != number2:
            # If they differ, increment the difference counter
            difference_count += 1
    
    # After comparing, check how many differences were found
    if difference_count < 3:
        print("YES")  # Print "YES" if fewer than three differences
    else:
        print("NO")   # Print "NO" if three or more differences

# Start the program by calling the main function
main()
