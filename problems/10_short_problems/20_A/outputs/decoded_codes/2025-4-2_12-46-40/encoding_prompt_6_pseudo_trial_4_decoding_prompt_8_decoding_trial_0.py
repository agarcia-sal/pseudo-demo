def main():
    # Step 1: Read input from the standard input (user)
    user_input = input()
    
    # Step 2: Normalize the input file path
    normalized_path = normalize_path(user_input)
    
    # Step 3: Adjust leading slashes
    if normalized_path.startswith('/'):
        normalized_path = replace_multiple_leading_slashes_with_one(normalized_path)

    # Step 4: Output the final normalized path
    print(normalized_path)

def normalize_path(input_path):
    # This function normalizes the given file path
    # This can include operations such as removing redundant slashes and resolving relative paths (like `..` and `.`)
    
    # Split the path into parts and filter out empty segments (which represent redundant slashes)
    parts = input_path.split('/')
    filtered_parts = [part for part in parts if part and part != '.']
    
    # Resolve `..`
    stack = []
    for part in filtered_parts:
        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    # Join the normalized parts back into a path
    normalized = '/' + '/'.join(stack)
    return normalized

def replace_multiple_leading_slashes_with_one(path):
    # This function replaces multiple leading slashes with a single slash
    while path.startswith('//'):
        path = path[1:]
    return path

if __name__ == "__main__":
    main()
