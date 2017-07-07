def fib (x):
    if x==1:
        return 1
    else:
        return x*fib(x-1)

c = input ("pick a number")
print(fib(int(c)))
