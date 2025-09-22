def process_email_string():
    # Step 1: Read Input
    input_string = input().strip()

    # Step 2: Replace Terms
    input_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Handle Leading Character
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]

    # Step 4: Initialize Variables
    countAt = 0
    outputList = []

    # Step 5: Check Leading Character for "at"
    if input_string.startswith('@'):
        input_string = "at" + input_string[1:]

    # Step 6: Process Each Character
    for char in input_string:
        if char == '@':
            if countAt > 0:
                outputList.append("at")
            else:
                outputList.append("@")
            countAt += 1
        else:
            outputList.append(char)
            countAt = 0  # Reset counter for non-@ characters

    # Step 7: Join and Finalize Output
    final_string = ''.join(outputList)
    
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Step 8: Print Output
    print(final_string)

# To execute the function and process the email string
process_email_string()
