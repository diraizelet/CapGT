def fibonacci(n):
    a=-1
    b=0
    c=1
    for i in range(n):
        if i==0:
            print(b,"\n",c)
        elif i==1:
            a=c+b
            b=c
            c=a
            continue
        else:
            print(a)
        a=c+b
        b=c
        c=a

def main():
    n=int(input("Enter the input: "))
    fibonacci(n)

main()