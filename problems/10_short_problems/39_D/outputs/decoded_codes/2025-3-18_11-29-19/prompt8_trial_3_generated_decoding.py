def main():
    # Read two lines of input, which represent two sequences of numbers
    sequence1 = input()
    sequence2 = input()

    # Split the input sequences into individual numbers and store them in lists
    numbers1 = sequence1.split()
    numbers2 = sequence2.split()

    # Initialize a counter to track the number of differences
    differenceCount = 0 

    # Loop through the first three numbers of both sequences
    for index in range(3):
        # Convert the numbers from the list into integers
        numberFromFirstSequence = int(numbers1[index])
        numberFromSecondSequence = int(numbers2[index])
        
        # Check if the numbers are different
        if numberFromFirstSequence != numberFromSecondSequence:
            # Increment the counter for differences
            differenceCount += 1 

    # After checking all numbers, determine if the differences are less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
if __name__ == "__main__":
    main()
