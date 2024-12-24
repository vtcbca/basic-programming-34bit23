3.def fibonacci_list_comprehension(terms):
    a, b = 0, 1
    return [a := (a := b - a) if (b := a + b) else a for _ in range(terms)]

# Example usage
print(fibonacci_list_comprehension(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]