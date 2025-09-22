def transformInput():
    # Read a line of input and remove any surrounding whitespace
    line = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@"
    line = line.replace("dot", ".")
    line = line.replace("at", "@")

    # If the first character is ".", prepend "dot" to the string
    if line and line[0] == ".":
        line = "dot" + line[1:]

    # Initialize variables for processing
    countAtSign = 0
    transformedList = []  # This will hold the processed characters
    length = len(line)

    # If the first character is "@", prepend "at" to the string
    if line and line[0] == "@":
        line = "at" + line[1:]

    # Iterate through each character in the transformed line
    for character in line:
        if character == "@":
            if countAtSign > 0:
                # Replace with "at" to prevent consecutive "at"
                transformedList.append("at")
                countAtSign = 1  # Count the occurrence of "at"
            else:
                # First occurrence of "@"
                transformedList.append("@")
                countAtSign = 1
        else:
            # Append the current character as is
            transformedList.append(character)

    # Join the transformed list into a single string
    finalString = ''.join(transformedList)

    # If the last character is ".", replace it with "dot"
    if finalString and finalString[-1] == ".":
        finalString = finalString[:-1] + "dot"

    # Output the final transformed string
    print(finalString)

# Unit test-like function to check various test cases
def test_transformInput():
    # Saving test cases as tuples of (input, expected_output)
    test_cases = [
        ("dot.example@domain.com", "dot.example@domain.com"),
        ("example.dot@domain", "example.dot@domain"),
        ("@example.com", "atexample.com"),
        ("..", "dot."),
        ("a@b@c", "a@b@c"),
        ("a@atb.c", "a@atb.c"),
        ("dot..text.", "dot.text.dot"),
        ("no.dots@here", "no.dots@here"),
        ("ending.with.dot.", "ending.with.dot"),
        ("multiple at here @@@@ test", "multiple at here at test")
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        # Simulate input() by overriding the input function temporarily
        import sys
        from io import StringIO

        input_backup = sys.stdin
        sys.stdin = StringIO(input_str)
        
        # Capture output
        from contextlib import redirect_stdout
        output = StringIO()
        with redirect_stdout(output):
            transformInput()
        
        # Check if the output matches the expected value
        assert output.getvalue().strip() == expected, f"Test case {i+1} failed: expected '{expected}', got '{output.getvalue().strip()}'"
        
        # Restore original input function
        sys.stdin = input_backup

# Uncomment the line below to run the tests
# test_transformInput()
