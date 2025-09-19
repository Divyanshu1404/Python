# n = 3
# width = 2 * n + 1

# # Top 3 rows
# for row in range(3):
#     if row == 0:  # First row
#         print("* " * n + "  " * n + "* " * n)
#     elif row == 1:  # Second row
#         print("  " * (n - 1) + "* " + "  " * n + "* ")
#     else:  # Third row
#         print("  " * (n - 1) + "* " * (2 * n - 1))

# # Rows with @
# for i in range(n):
#     for j in range(2 * n + 1):
#         if j == n + 1:
#             print("@ ", end="")
#         else:
#             print("  ", end="")
#     print()


# n=5
# for i in range(n-2):
#     for j in range(i+1):
#         print("*",end='')
#     print()
# print("*"*(n-1),end='')
# print(" "*(n+1),end='')
# print("*")
# print("*"*(2*n+2))
# print("*"*(n-1),end='')
# print(" "*(n+1),end='')
# print("*")

# for i in range(n):
#     for j in range(n-i-2):
#         print("*",end='')

#     print()              


n=5
for i in range(n+1):
    for j in range(i):
        print('*',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(n):
        if(i==n):
            print('@',end='')
        else:
            print(' ',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()

for i in range(n-1):5
for j in range(3 * n):
        if(j<n or j>2*n-1):
            print(' ',end='')
        else:
            print('@',end='')
    print()
for i in range(n//2+1):
    for j in range(n):
        print(' ',end='')
    for j in range(i):
        print(' ',end='')
    for j in range(n-2*i):
        print('*',end='')
    for j in range(i):
        print(' ',end='')
    for j in range(n):
        print(' ',end='')
    print()


