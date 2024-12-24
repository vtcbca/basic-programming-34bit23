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