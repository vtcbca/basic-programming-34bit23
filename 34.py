solution

1.import math

def factorial_math_module(n):
    return math.factorial(n)

# Example usage
print(factorial_math_module(5))  # Output: 120


2.import math

def is_prime_sqrt(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime_sqrt(11))  # Output: True
print(is_prime_sqrt(15))  # Output: False


3.def fibonacci_list_comprehension(terms):
    a, b = 0, 1
    return [a := (a := b - a) if (b := a + b) else a for _ in range(terms)]

# Example usage
print(fibonacci_list_comprehension(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


4.def reverse_string_reversed(s):
    return ''.join(reversed(s))

# Example usage
print(reverse_string_reversed("hello"))  # Output: "olleh"


5.def is_palindrome_reversed(s):
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    return s == ''.join(reversed(s))

# Example usage
print(is_palindrome_reversed("A man a plan a canal Panama"))  # Output: True
print(is_palindrome_reversed("hello"))  # Output: False


6.def pattern_recursive(n, i=1):
    if i > n:
        return
    print('* ' * i)
    pattern_recursive(n, i + 1)

# Example usage
pattern_recursive(4)


7.def triangle_recursive(n, i=1):
    if i > n:
        return
    print(' ' * (n - i) + ' '.join(str(x) for x in range(1, 2 * i)))
    triangle_recursive(n, i + 1)

# Example usage
triangle_recursive(3)


8.def print_row(i, n):
    if i > n:
        return
    # Calculate spaces for the current row
    spaces = ' ' * (n - i) * 2
    
    # Create the alphabet sequence
    forward_seq = [chr(65 + j) for j in range(i)]  # A, B, C, ...
    backward_seq = forward_seq[:-1][::-1]  # A, B, ... and then reversed
    
    # Combine forward and backward sequence
    row = forward_seq + backward_seq
    
    # Print the row with spaces
    print(spaces + '   '.join(row))
    
    # Recursive call
    print_row(i + 1, n)

def alphabet_pattern_recursive(n):
    print_row(1, n)

# Example usage
alphabet_pattern_recursive(3)
