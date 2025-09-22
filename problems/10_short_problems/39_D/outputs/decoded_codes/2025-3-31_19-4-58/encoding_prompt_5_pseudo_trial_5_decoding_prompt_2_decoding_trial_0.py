def main():
    # Read two lines of input from the user, each containing three numbers
    firstSet = input()
    secondSet = input()

    # Split the input strings into separate numbers
    firstNumbers = firstSet.split()
    secondNumbers = secondSet.split()

    # Initialize a count to track the number of differences
    differenceCount = 0 

    # Loop through the numbers in the two sets
    for index in range(3):
        # Convert the current numbers from strings to integers
        firstNumber = int(firstNumbers[index])
        secondNumber = int(secondNumbers[index])
        
        # Check if the current numbers from both sets are different
        if firstNumber != secondNumber:
            # Increment the difference count if they are different
            differenceCount += 1
    
    # After comparing all numbers, check the difference count
    if differenceCount < 3:
        # If there are fewer than three differences, output "YES"
        print("YES")
    else:
        # If there are three or more differences, output "NO"
        print("NO")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
