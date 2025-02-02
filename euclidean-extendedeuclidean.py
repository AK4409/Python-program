def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    gcd = euclidean_gcd(a, b)
    print(f"GCD using Euclidean Algorithm: {gcd}")
    
    ext_gcd, x, y = extended_euclidean(a, b)
    print(f"GCD using Extended Euclidean Algorithm: {ext_gcd}")
    print(f"Coefficients x and y (for equation ax + by = gcd(a, b)): x = {x}, y = {y}")
