import re

def normalize_and_print_path():
    # Read input from standard input
    raw_input = input()
    
    # Normalize the input path
    normalized_path = normalize_path(raw_input)
    
    # Print the modified path, replacing multiple leading slashes with a single slash
    print(replace_leading_slashes(normalized_path))

def normalize_path(raw_input):
    # Remove any leading or trailing whitespace from the input
    trimmed_input = raw_input.strip()
    
    # Normalize the file path, this includes resolving '.', '..' and other path components
    normalized_path = standard_path_normalization(trimmed_input)
    
    return normalized_path

def replace_leading_slashes(path):
    # Use a regular expression to replace multiple leading slashes with a single slash
    modified_path = re.sub(r'^/+', '/', path)
    
    return modified_path

def standard_path_normalization(path):
    # This function resolves '.', '..' and simplifies the path
    parts = path.split('/')
    stack = []
    
    for part in parts:
        if part == '' or part == '.':
            # Ignore empty parts and current directory references
            continue
        elif part == '..':
            # Go up one directory, if possible
            if stack:
                stack.pop()
        else:
            # Add the valid directory to the stack
            stack.append(part)
    
    # Join the normalized components into a single path
    normalized = '/'.join(stack)
    
    return normalized

# Testing practices
if __name__ == "__main__":
    # Example test cases
    test_paths = [
        "/a/b/c/../../d",        # Should normalize to "/a/d"
        "////a//b/c//..//",     # Should normalize to "/a/b"
        "a/b/./c/../",          # Should normalize to "a/b"
        "//../a//b/c/",         # Should normalize to "/a/b/c"
        "   /some/path/    "    # Should normalize to "/some/path"
    ]
    
    for test in test_paths:
        print(f"Original: '{test}' => Normalized: ", end='')
        normalized_path = normalize_and_print_path(test)
        print(normalized_path)
