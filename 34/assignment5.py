5.def is_palindrome_reversed(s):
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    return s == ''.join(reversed(s))

# Example usage
print(is_palindrome_reversed("A man a plan a canal Panama"))  # Output: True
print(is_palindrome_reversed("hello"))  # Output: False