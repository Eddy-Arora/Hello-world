def stars(n):
    for i in range(n):
        for j in range(0, i+1):

            print("*", end="")
            print()
def main():
    for i in range(5,-1,-1):
        stars(i+1)

main()

