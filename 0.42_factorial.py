# 3! =3x2x1
# 3! =1x2x3
# 5! =5x4x3x2x1

def get_factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i

    return fact
    

def main():
    print(f"3! = {get_factorial(3)}")
    print(f"5! = {get_factorial(5)}")
    
main()