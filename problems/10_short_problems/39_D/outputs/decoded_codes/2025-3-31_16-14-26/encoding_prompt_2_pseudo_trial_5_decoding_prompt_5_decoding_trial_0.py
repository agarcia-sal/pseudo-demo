# Main process to compare two sets of inputs
def main():
    # Read input strings from the user
    inputString1 = input()
    inputString2 = input()
    
    # Split the input strings into lists of tokens
    tokens1 = inputString1.split()
    tokens2 = inputString2.split()
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Compare the first three entries from both lists
    for index in range(3):
        # Convert tokens to integers
        valueFromFirstInput = int(tokens1[index])
        valueFromSecondInput = int(tokens2[index])
        
        # Check if values are different and increment the counter if they are
        if valueFromFirstInput != valueFromSecondInput:
            differenceCount += 1
    
    # Check the difference count and return the appropriate output
    if differenceCount < 3:
        print("YES")  # Fewer than three differences
    else:
        print("NO")   # Three or more differences

# Entry point for the script
if __name__ == "__main__":
    main()
