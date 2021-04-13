def get_sum_of_cubes(n):
    sum = 0
    i = 1
    while i in range(1, n+1):
        sum = sum + i * i * i
        i = i + 1

    return sum

def main():
    n = int((input("enter n: ")))
    sum = get_sum_of_cubes(n)
    print(f"sum of cubes of first {n} Natural numbers = {sum}")

main()