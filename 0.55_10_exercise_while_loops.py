i = "_"
def print_line(n):
    while i in range(n):
        print("_", end="")
    print()

def main():
    while i in range(20):
        print_line(i)

main()