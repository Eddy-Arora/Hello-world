def print_interest(p,n,r):
    si = (p*n*r)/100
    print(f"simple intetest is = {si} %")

def main():
    p = int(input("Enter p: "))
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    
    print_interest(p,n,r)

main()


##Accept p, n and r
##si = pnr/100
##print si
