6.def pattern_recursive(n, i=1):
    if i > n:
        return
    print('* ' * i)
    pattern_recursive(n, i + 1)

# Example usage
pattern_recursive(4)
