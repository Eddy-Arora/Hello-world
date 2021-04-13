def get_reverse(n):
    rev = 0
    i = n
    while i > 0:
        rem = i % 10
        rev = rev * 10 + rem
        i = i // 10
    return rev

def main():
    print(f"1234 <--> {get_reverse(1234)} ")
    print(f"8441 <--> {get_reverse(8441)} ")
    
main()
