def get_sum(n):
    sum = 0
    i = 1
    while i in range(n+1):
        sum = sum + i
        i = i + 1

    return sum

def main():
    n = int((input("enter n: ")))
    sum = get_sum(n)
    print(f"sum of first {n} Natural numbers = {sum}")

main()