def main():
    # Step 1: Read the input file path from standard input
    userInput = input()

    # Step 2: Normalize the input path
    normalizedPath = NormalizePath(userInput)

    # Step 3: Ensure the normalized path starts with a single '/'
    finalPath = ReplaceMultipleLeadingSlashes(normalizedPath)

    # Step 4: Print the final normalized path
    print(finalPath)

def NormalizePath(inputPath):
    # Split the path by slashes and filter out empty segments and '.' 
    # Also handle '..' by keeping track of the current directory level
    parts = inputPath.split('/')
    stack = []
    
    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()  # Go up to the parent directory if possible
        else:
            stack.append(part)  # Add valid directory names to the stack

    # Join the filtered parts back together with slashes
    normalizedInputPath = '/'.join(stack)
    return normalizedInputPath

def ReplaceMultipleLeadingSlashes(path):
    # Replace multiple leading slashes with a single '/', adhering to the specified conditions
    if path.startswith('/'):
        return '/' + path.lstrip('/')  # Remove leading slashes and keep one
    else:
        return '/' + path  # Prepend a single slash if none exists

# Call the main function to execute the code
main()
