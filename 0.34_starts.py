def print_star_triangle(n):
    for i in range(n):
        print("*", end="")
    print()

def main():
    for i in range(5, -1, -1):
        print_star_triangle(i+1)

main()




