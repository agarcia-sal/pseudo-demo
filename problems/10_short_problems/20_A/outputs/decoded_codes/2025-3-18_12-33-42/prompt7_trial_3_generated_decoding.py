def processInputPath():
    # Read input from standard input
    inputPath = input()  
    # Normalize the path to remove redundant separators and up-level references
    normalizedPath = normalizePath(inputPath)
    # Remove leading slashes from the normalized path, replacing them with a single leading slash
    finalPath = removeLeadingSlashes(normalizedPath)
    # Print the final cleaned path
    print(finalPath)

def normalizePath(path):
    # Split the path by the slashes to process each component
    components = path.split('/')
    stack = []
    for component in components:
        # Ignore empty components and those which are just '.'
        if component == '' or component == '.':
            continue
        # If the component is '..', pop from the stack if there's something to pop
        if component == '..':
            if stack:
                stack.pop()
        else:
            # Otherwise, it's a valid directory name - push onto the stack
            stack.append(component)
    # Join the components back into a normalized path
    # Return it with leading '/' if stack is not empty, otherwise just the empty path
    return '/' + '/'.join(stack) if stack else '/'

def removeLeadingSlashes(path):
    # Check if the path starts with a slash and does not have multiple leading slashes
    # Return the path ensuring it starts with one slash
    return '/' + path.lstrip('/')

# The following lines are for testing the functions and would typically not be included in a library/module
if __name__ == "__main__":
    # Example cases to demonstrate functionality:
    test_paths = [
        "/usr//bin/./scripts/../",
        "//var//log///",
        "/../a/b/../c/",
        "////home/user//documents//",
        "/etc///config//..//",
        "relative/path/without/slashes",
        "////"
    ]
    
    for test in test_paths:
        print(f"Input Path: '{test}' => Normalized Path: '{processInputPath(test)}'")
