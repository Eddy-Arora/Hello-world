def is_perfect(n):
    i=1
    rem=0
    sum=0
    
    while i<n:
        rem=n%i
        if rem==0:
            sum=sum+i
            
        i+=1
    if sum==n:
        
        return 1
    else:
        
        return 0

def main():
    n=int(input("Enter the value of n: "))
    for num in range(1, n+1, 1):
        if is_perfect(num):
            print(num)
        

main()