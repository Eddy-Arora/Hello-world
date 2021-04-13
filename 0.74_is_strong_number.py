def get_factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i

    return fact

def is_strong(n):
    i = n
    sum = 0
    while i > 0:
        rem = i % 10
        sum += get_factorial(rem)
        i = i // 10

    return n ==sum

def main():
    print("Is strong number: ")
    print(f"1 --> {is_strong(1)}")
    print(f"2 --> {is_strong(1)}")
    print(f"145 --> {is_strong(1)}")
    print(f"146 --> {is_strong(1)}")
    print(f"370 --> {is_strong(1)}")
    
    
main()
