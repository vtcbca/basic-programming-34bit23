7.def triangle_recursive(n, i=1):
    if i > n:
        return
    print(' ' * (n - i) + ' '.join(str(x) for x in range(1, 2 * i)))
    triangle_recursive(n, i + 1)

# Example usage
triangle_recursive(3)