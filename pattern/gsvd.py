n=5
for i in range(2*n):
    if i < n:
        print("@", end="")
    else:
        print(" ", end="")
    if i >= n//2 and i < n + n//2:
        print(" "*(n-1)*(i-n//2), "*"*(n), " "*(((n*(n-1))-(n-1))-((n-1)*(i-n//2))), sep="", end="")
    else:
        print(" "*(n*(n-1)+1), end="")
    if i >= n-1:
        print("@", end="")
    else:
        print(" ", end="")
    print()