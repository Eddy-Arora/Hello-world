def print_interest(p,n,r):
    si = (p*n*r)/100
    i = 0
    while(i<= si):
        si = (((p*n*r)/100)+1-1) 
        i = i + 1
        print(f"simple interest is = {si} %")

def main():
    p = int(input("Enter p: "))
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    
    print_interest(p,n,r)

main()
