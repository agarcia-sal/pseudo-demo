def main():
    # Read two lines of input
    string1 = input()
    string2 = input()

    # Split the input strings into lists of string numbers
    numbers1 = string1.split()
    numbers2 = string2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string numbers to integers
        num1 = int(numbers1[index])
        num2 = int(numbers2[index])
        
        # Check if the numbers are different
        if num1 != num2:
            difference_count += 1

    # Evaluate the number of differences to determine the output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
